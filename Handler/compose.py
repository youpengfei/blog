# -*- coding: utf-8 -*-
from bson import ObjectId
from datetime import datetime
import markdown
import tornado.web


from handler.base import BaseHandler

__author__ = 'youpengfei'


class ComposeHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        id = self.get_argument("id", None)
        entry = None
        if id:
            entry = self.mongo["blog"].post.find_one({"_id": ObjectId(id)})
        self.render("admin/compose.html", entry=entry)

    @tornado.web.authenticated
    def post(self):
        id = self.get_argument("id", None)
        entry = None
        title = self.get_argument("title")
        content = self.get_argument("content")
        tags = self.get_argument("tags")
        category_id = self.get_argument("categoryId")
        brief = self.get_argument("brief", "暂无介绍")
        user = self.get_current_user()

        html = markdown.markdown(content, extensions=(['codehilite(css_class=highlight)', 'extra', 'fenced_code', 'tables', 'sane_lists']))
        post = {
            "title": title,
            "content": html,
            "tags": tags.split(","),
            "category_id": [1, 2],
            "author": user["name"],
            "brief": brief,
            "markDown": content,
            "published": datetime.now()
        }
        one = self.mongo["blog"].post.find_one({"_id": ObjectId(id)})
        if one is not None:
            self.mongo["blog"].post.update({"_id": ObjectId(id)}, {"$set": post})
            self.redirect("/")
        else:
            self.mongo["blog"].post.insert(post)


