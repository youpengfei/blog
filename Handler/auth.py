# -*- coding: utf-8 -*-
import tornado.web
from handler.base import BaseHandler
import tornado.auth

__author__ = 'youpengfei'


class AuthLoginHandler(BaseHandler, tornado.auth.GoogleMixin):
    @tornado.web.asynchronous
    def get(self):
        if self.get_argument("openid.mode", None):
            self.get_authenticated_user(self.async_callback(self._on_auth))
            return
        self.authenticate_redirect()

    def _on_auth(self, user):
        if not user:
            raise tornado.web.HTTPError(500, "Google auth failed")
        author = self.mongo['blog'].author.find_one({"email": user["email"]})
        if not author:
            # Auto-create first author
            any_author = self.mongo["blog"].author.find_one()
            if not any_author:
                author_id = self.mongo['blog'].author.insert({"email": user["email"], "name": user["name"]})
            else:
                self.redirect("/")
                return
        else:
            author_id = author["_id"]
        self.set_secure_cookie("blogdemo_user", author["email"])
        self.redirect(self.get_argument("next", "/"))


class AuthLogoutHandler(BaseHandler):
    def get(self):
        self.clear_cookie("blogdemo_user")
        self.redirect(self.get_argument("next", "/"))