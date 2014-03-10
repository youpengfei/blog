# -*- coding: utf-8 -*-
from handler.Config import PAGE_SIZE

__author__ = 'youpengfei'
import tornado.web


class BaseUIModule(tornado.web.UIModule):
    @property
    def db(self):
        return self.handler.application.db


class TagModule(BaseUIModule):
    def render(self):
        tags = self.db.query("select * from tag")
        return self.render_string("modules/tags.html", tags=tags)


class LinkModule(BaseUIModule):
    def render(self):
        links = self.db.query("select * from link")
        return self.render_string("modules/links.html", links=links)


class CategoryModule(BaseUIModule):
    def render(self):
        categories = self.db.query("select * from category")
        return self.render_string("modules/categories.html", categories=categories)


class PaginationModule(BaseUIModule):
    def render(self):
        current_page = int(self.handler.get_argument("pageNum", 1))
        count = self.db.get("SELECT count(1) as row FROM blog")["row"]
        pages = count / PAGE_SIZE if count % PAGE_SIZE == 0 else  count / PAGE_SIZE + 1
        return self.render_string("modules/pagination.html", currentPage=current_page, pages=pages)


