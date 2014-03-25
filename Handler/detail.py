# -*- coding: utf-8 -*-
from bson import ObjectId
from handler.base import BaseHandler

__author__ = 'youpengfei'


class DetailHandler(BaseHandler):
    def get(self, id):
        article = self.mongo["blog"].post.find_one({"_id": ObjectId(id)})
        self.render("detail.html", article=article)
