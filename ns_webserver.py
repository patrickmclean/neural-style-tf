import os, os.path
import random
import string
import json

import cherrypy
from neural_style_web import launchNeuralStyle

# Return index page (this is just for reference)
class PageLoader(object):
    @cherrypy.expose
    def index(self):
        return open('index.html')

# Call neural styles
@cherrypy.expose
class WebServiceLoader(object):

    @cherrypy.tools.accept(media='application/x-www-form-urlencoded')
    def POST(self,inputFile,referenceFile,outputFile):
        print('called '+inputFile)
        # somewhat hacky way of going asynchronous. Split this process in two, 
        # one returns immediately, the other does the processing
        child_pid = os.fork()
        if child_pid == 0:
            # new process
            print('new process')
            launchNeuralStyle(inputFile, referenceFile,outputFile)
        else:
            # existing process
            
            response = ('{"output":"%s"}' % outputFile)
            print('existing process '+response)
            return json.dumps(response).encode('utf8')

if __name__ == '__main__':
    conf = {
        '/': {
            'tools.sessions.on': True,
            'tools.staticdir.root': os.path.abspath(os.getcwd())
        },
        '/neuralstyle': {
            'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
            'tools.response_headers.on': True,
            'tools.response_headers.headers': [('Content-Type', 'application/x-www-form-urlencoded; charset=utf-8')],
        },
    }
    webapp = PageLoader()
    webapp.neuralstyle = WebServiceLoader()
    cherrypy.config.update({'server.socket_host': '0.0.0.0', #this makes it transmit through host
                            'server.socket_port':8082})
    cherrypy.quickstart(webapp, '/', conf)