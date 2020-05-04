
import tornado.ioloop
import tornado.web
import netifaces as ni


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        #return the ip address the the network inteface
        ip = ni.ifaddresses('eth0')[ni.AF_INET][0]['addr']
        self.write(ip)


def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
