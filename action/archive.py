# -*- coding: utf-8 -*-
from action.base import BaseHandler

__author__ = 'youpengfei'

class ArchiveHandler(BaseHandler):
    def get(self):
        entries = self.db.query("SELECT * FROM blog ORDER BY published "
                                "DESC")
        active="allArticle"
        self.render("archive.html", entries=entries,active=active)