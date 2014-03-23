# -*- coding: utf-8 -*-
import sys

__author__ = 'youpengfei'

import qiniuTest.conf

qiniuTest.conf.ACCESS_KEY = "LYgEIxfrKt7h6tf2ero1VrtwxxqUr1qmIuqhiV2n"
qiniuTest.conf.SECRET_KEY = "PTihHOOPlnNDgoi25fo4x7JvSZ8lX2zAw3cqXuUX"

import qiniuTest.io

localfile = "/Users/youpengfei/tempFile/FreeMarker_Manual_zh_CN.pdf"

policy = qiniuTest.rs.PutPolicy("image")
uptoken = policy.token()

ret, err = qiniuTest.io.put_file(uptoken, "FreeMarker_Manual_zh_CN", localfile)
if err is not None:
    sys.stderr.write('error: %s ' % err)
