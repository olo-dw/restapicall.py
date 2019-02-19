#!/usr/bin/env python
# -*-coding:UTF-8 -*
#
# Olivier Locard

import requests

from restapicall.utils import Utils


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

    def get(self):
        return requests.get(self.get_url())

    def get_url(self):
        return Utils.build_uri(self.endpoint, self.uri, self.args)


if __name__ == '__main__':
    conn = ApiCall('http://example.org')
    r = conn.get()
    print(r.status_code)
    print(r.headers['content-type'])
