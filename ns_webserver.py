import os, os.path
import random
import string
import json
import time

import cherrypy
from neural_style_web import launchNeuralStyle
from awss3 import s3Download

# Return index page (this is just for reference)
class PageLoader(object):
    @cherrypy.expose
    def index(self):
        return open('index.html')

# Serverstream, to send completed status back when processing is done
    @cherrypy.expose
    def getstatus(self):
        cherrypy.response.headers["Content-Type"] = "text/event-stream"
        def generator():
            statusFile = open('status_file',"r")
            while True:
                # Best (horrible) idea so far. Poll here for the file system and send back status
                time.sleep(5)
                statusFile.seek(0,0)
                status = statusFile.read()
                yield "event: time\n" + "data: " + str(time.time()) + " " + status + "\n\n"
        return generator()
    getstatus._cp_config = {'response.stream': True}

# Call neural styles
@cherrypy.expose
class WebServiceLoader(object):

    @cherrypy.tools.accept(media='application/x-www-form-urlencoded')
    def POST(self,inputFile,referenceFile,outputFile):
        print('called '+inputFile+" "+referenceFile)
        # somewhat hacky way of going asynchronous. Split this process in two, 
        # one returns immediately, the other does the processing
        child_pid = os.fork()
        if child_pid == 0:
            # new process
            response = ('{"output":"%s"}' % outputFile)
            print('existing process '+response)
            return json.dumps(response).encode('utf8')            
        else:
            # existing process
            print('new process')
            # download the files first
            s3Download('input',inputFile)
            s3Download('reference',referenceFile)
            launchNeuralStyle(inputFile, referenceFile,outputFile)
            # when we're done we need to add an upload


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