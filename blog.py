import os.path
import tornado.auth
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

from tornado.options import define, options
from handler.aboutme import AboutMeHandler
from handler.auth import AuthLoginHandler, AuthLogoutHandler
from handler.compose import ComposeHandler
from handler.detail import DetailHandler
from handler.entry import EntryHandler
from handler.fileupload import FileUpload
from handler.home import HomeHandler
from handler.archive import ArchiveHandler
from handler.preview import PreviewHandler
from modules import PaginationModule
from pymongo import MongoClient

define("port", default=8999, help="run on the given port", type=int)
define("mysql_host", default="127.0.0.1:3306", help="blog database host")
define("mysql_database", default="blog", help="blog database name")
define("mysql_user", default="blog", help="blog database user")
define("mysql_password", default="blog", help="blog database password")


class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/", HomeHandler),
            (r"/entry/([^/]+)", EntryHandler),
            (r"/compose", ComposeHandler),
            (r"/auth/login", AuthLoginHandler),
            (r"/auth/logout", AuthLogoutHandler),
            (r"/detail/(.+)", DetailHandler),
            (r"/aboutMe", AboutMeHandler),
            (r"/archives", ArchiveHandler),
            (r"/preview", PreviewHandler),
            (r"/file", FileUpload),
        ]
        settings = dict(
            blog_title=u"worldCode",
            author="youpengfei",
            lang="zh",
            default_url="worldcode.cn",
            template_path=os.path.join(os.path.dirname(__file__), "templates"),
            static_path=os.path.join(os.path.dirname(__file__), "static"),
            xsrf_cookies=True,
            cookie_secret="__TODO:_GENERATE_YOUR_OWN_RANDOM_VALUE_HERE__",
            login_url="/auth/login",
            debug=True,
            ui_modules={'pagination': PaginationModule},
        )

        tornado.web.Application.__init__(self, handlers, **settings)

        # Have one global connection to the blog DB across all handlers
        # self.db = torndb.Connection(
        #     host=options.mysql_host, database=options.mysql_database,
        #     user=options.mysql_user, password=options.mysql_password)
        self.mongo = MongoClient("192.168.1.101")


def main():
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()


if __name__ == "__main__":
    main()


