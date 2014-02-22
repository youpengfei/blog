# -*- coding: utf-8 -*-
import tornado.web

__author__ = 'youpengfei'


class ItemModule(tornado.web.UIModule):
    def render(self, entry):
        tags = []
        if entry['tags']:
            tags = entry["tags"].split(",")
        return self.render_string("item.html", entry=entry, tags=tags)