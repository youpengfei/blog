# -*- coding: utf-8 -*-
from handler.base import BaseHandler

__author__ = 'youpengfei'


class DetailHandler(BaseHandler):
    def get(self, id):
        article = self.db.get("SELECT * FROM blog WHERE id = %s", id)
        self.render("article.html", active="home", article=article)
