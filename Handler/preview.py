# -*- coding: utf-8 -*-
from datetime import datetime
import markdown
from handler.base import BaseHandler

__author__ = 'youpengfei'


class PreviewHandler(BaseHandler):
    def post(self, *args, **kwargs):
        title = self.get_argument("title")
        content = self.get_argument("content")
        tags = self.get_argument("tags")
        category_id = self.get_argument("categoryId")
        brief = self.get_argument("brief", "暂无介绍")
        user = self.get_current_user()
        html = markdown.markdown(content, extensions=(
            ['codehilite(css_class=highlight)', 'extra', 'fenced_code', 'tables', 'sane_lists']))
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
        return self.render("preview.html", article=post)
