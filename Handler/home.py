# -*- coding: utf-8 -*-

from handler.Config import PAGE_SIZE
from handler.base import BaseHandler

__author__ = 'youpengfei'


class HomeHandler(BaseHandler):
    def get(self):
        current_page = int(self.get_argument("pageNum", 1))
        begin_index = (current_page - 1) * PAGE_SIZE;
        items = [row for row in self.mongo["blog"].post.find().skip(begin_index).limit(PAGE_SIZE)]
        self.render("index.html", items=items)