#!/usr/bin/env python
# -*-coding:UTF-8 -*
#
# Olivier Locard


class ApiCall(object):

    def __init__(self, endpoint, uri=None, args={}):
        self.endpoint = endpoint
        self.args = args
        if uri is None:
            self.uri = ()
        else:
            self.uri = uri

    def __str__(self):
        return str(dict(endpoint=self.endpoint, uri=self.uri, args=self.args))
