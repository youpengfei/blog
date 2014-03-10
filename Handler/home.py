# -*- coding: utf-8 -*-
from handler.Config import PAGE_SIZE
from handler.base import BaseHandler

__author__ = 'youpengfei'


class HomeHandler(BaseHandler):
    def get(self):
        current_page = int(self.get_argument("pageNum", 1))
        begin_index = (current_page - 1) * 2;
        items = self.db.query("SELECT * FROM blog ORDER BY published DESC limit %s,%s", begin_index, PAGE_SIZE)
        self.render("index.html", items=items)