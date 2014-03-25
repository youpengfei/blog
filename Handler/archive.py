# -*- coding: utf-8 -*-
from handler.base import BaseHandler

__author__ = 'youpengfei'


class ArchiveHandler(BaseHandler):
    def get(self):
        courser = self.mongo["blog"].post.find()
        entries = [x for x in courser]
        courser.close()
        self.render("archives.html", entries=entries)