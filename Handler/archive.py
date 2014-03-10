# -*- coding: utf-8 -*-
from handler.base import BaseHandler

__author__ = 'youpengfei'

class ArchiveHandler(BaseHandler):
    def get(self):
        entries = self.db.query("SELECT * FROM blog ORDER BY published "
                                "DESC")
        self.render("archives.html", entries=entries)