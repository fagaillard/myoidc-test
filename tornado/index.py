
import tornado.ioloop
import tornado.web
import netifaces as ni


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        #return the ip address the the network inteface
        ip = ni.ifaddresses('eth0')[ni.AF_INET][0]['addr']

        html = "<html><head><title>Sample OIDC app</title></head><body>"
        html = html + "<p>My Pod Ip address is " + ip + "</p>"
        html = html + "<p>Avalaible HTTP Headers</p><pre>"
        for key, value in self.request.headers.items():
          html = html + key + " : " + value + "\n"
        html = html + "</pre></body></html>"
        self.write(html)


def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])


if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
