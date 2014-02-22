# -*- coding: utf-8 -*-
import tornado.web
from action.base import BaseHandler

__author__ = 'youpengfei'
class EntryHandler(BaseHandler):
    def get(self, slug):
        entry = self.db.get("SELECT * FROM entries WHERE slug = %s", slug)
        if not entry: raise tornado.web.HTTPError(404)
        self.render("entry.html", entry=entry)