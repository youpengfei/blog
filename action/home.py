# -*- coding: utf-8 -*-
from action.base import BaseHandler

__author__ = 'youpengfei'


class HomeHandler(BaseHandler):
    def get(self):
        items = self.db.query("SELECT * FROM blog ORDER BY published DESC")
        active = "home"
        self.render("index.html", items=items, active=active)