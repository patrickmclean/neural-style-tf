import cherrypy, time

class Root():

    @cherrypy.expose
    def index(self):
        return r'''<!DOCTYPE html>
<html>
 <head>
  <title>Server-sent events test</title>
  <style>html,body,#test{height:98%;}</style>
 </head>
 <body>
  <script type="text/javascript">
    document.addEventListener('DOMContentLoaded', function () {
      var source = new EventSource('gettime');
      source.addEventListener('time', function (event) {
        document.getElementById('test').innerHTML += event.data + "\n";
      });
      source.addEventListener('error', function (event){
        console.log('SSE error:', event);
        console.log('SSE state:', source.readyState);
      });
    }, false);
  </script>
  <textarea id="test"></textarea>
 </body>
</html>'''

    @cherrypy.expose
    def gettime(self):
        cherrypy.response.headers["Content-Type"] = "text/event-stream"
        def generator():
            while True:
                time.sleep(1)
                yield "event: time\n" + "data: " + str(time.time()) + "\n\n"
        return generator()
    gettime._cp_config = {'response.stream': True}

if __name__ == '__main__':
    cherrypy.config.update({'server.socket_host': '0.0.0.0','server.socket_port':8082})
    cherrypy.quickstart(Root())
