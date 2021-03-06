import tornado.web;
import tornado.ioloop;

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello MainHandler")

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ]);

if __name__ == "__main__":
    app = make_app()
    app.listen(8800)
    tornado.ioloop.IOLoop.current().start()