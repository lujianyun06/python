#-*-encoding:utf-8-*-

import tornado.ioloop, tornado.web, tornado.httpserver
import json, os

local_host = "192.168.1.209"
file_data = ""
file_name = "WechatIMG13 2_converted.png"
file = None

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")

    '''
    上传
    '''
    def post(self, *args, **kwargs):
        pass
        file = self.request.files['file']
        fbody = file[0]['body']
        fname = file[0]['filename']
        ftype = file[0]['content_type']
        file_len = len(fbody)
        a = 10
        self.set_header('Content-Type', 'application/json; charset=UTF-8')
        self.write(json.dumps({'message': 'ok', 'code': '200', 's_size': "%s", 'f_size': "%s"}) % (10, file_len))
        self.finish(None)

    def put(self, *args, **kwargs):
        pass
        file = self.request.body
        a = 10


class HelloHandler(tornado.web.RequestHandler):
    '''
    下载
    '''
    def get(self, *args, **kwargs):
        a = self.request.uri
        print self.request.method + " " + str(self.request.headers) + " " + str(self.request.body)
        file_name = self.get_query_argument('file_name')
        self.set_header('Content-Type', 'application/octet-stream')
        self.set_header('Content-Disposition', 'attachment; filename=' + file_name)

        # buffer_size = file.__sizeof__()
        while True:
            buffer = file.read(1024)
            if not buffer:
                file.seek(0)
                break
            self.write(buffer)
        self.finish()


def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/hello/", HelloHandler)
    ])

if __name__ == "__main__":
    os.chdir("/Users/ljy/PycharmProjects/work")
    file = open(file_name, "rb")

    app = make_app()
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(8888, local_host)
    # app.listen(8888, industry_host)
    tornado.ioloop.IOLoop.current().start()
