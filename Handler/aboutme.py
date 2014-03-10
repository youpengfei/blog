# -*- coding: utf-8 -*-
from handler.base import BaseHandler

__author__ = 'youpengfei'


class AboutMeHandler(BaseHandler):
    def get(self):
        self.render("about-me.html")
