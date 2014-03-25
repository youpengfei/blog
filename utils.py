# -*- coding: utf-8 -*-
import functools

__author__ = 'youpengfei'

def myauthenticated(method):
    """Decorate methods with this to require that the user be logged in.

    If the user is not logged in, they will be redirected to the configured
    `login url <RequestHandler.get_login_url>`.
    """
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):

        return wrapper
