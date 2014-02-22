# -*- coding: utf-8 -*-
from action.base import BaseHandler

__author__ = 'youpengfei'


class AboutMeHandler(BaseHandler):
    def get(self, *args, **kwargs):
        active = "about"
        self.render("about-me.html", active=active)
