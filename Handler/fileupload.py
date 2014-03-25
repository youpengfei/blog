# -*- coding: utf-8 -*-
from lib2to3.pgen2.tokenize import String

from handler.base import BaseHandler

__author__ = 'youpengfei'


class FileUpload(BaseHandler):
    def post(self, *args, **kwargs):
        if self.request.files:
            for f in self.request.files['reqFile']:
                # write a file
                output = open("尤鹏飞.doc", mode="wb")
                output.write(f['body'])



