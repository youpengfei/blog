# -*- coding: utf-8 -*-
from handler.Config import PAGE_SIZE

__author__ = 'youpengfei'
import tornado.web


class BaseUIModule(tornado.web.UIModule):
    @property
    def db(self):
        return self.handler.application.mongo["blog"].post

class PaginationModule(BaseUIModule):
    def render(self):
        current_page = int(self.handler.get_argument("pageNum", 1))
        count = self.db.count()
        pages = count / PAGE_SIZE if count % PAGE_SIZE == 0 else  count / PAGE_SIZE + 1
        return self.render_string("modules/pagination.html", currentPage=int(current_page), pages=int(pages))


