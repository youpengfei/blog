# -*- coding: utf-8 -*-
import markdown

from handler.base import BaseHandler
import tornado.web

__author__ = 'youpengfei'




class FeedHandler(BaseHandler):
    def get(self):
        entries = self.db.query("SELECT * FROM entries ORDER BY published "
                                "DESC LIMIT 10")
        self.set_header("Content-Type", "application/atom+xml")
        self.render("feed.xml", entries=entries)

