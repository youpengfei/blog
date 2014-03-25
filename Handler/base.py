# -*- coding: utf-8 -*-

__author__ = 'youpengfei'
import tornado.web


class BaseHandler(tornado.web.RequestHandler):
    @property
    def mongo(self):
        return self.application.mongo

    def get_current_user(self):
        email = self.get_secure_cookie("blogdemo_user")
        if not email:
            return None
        return self.mongo['blog'].author.find({"email": email})