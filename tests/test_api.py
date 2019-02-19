#!/usr/bin/env python
# -*-coding:UTF-8 -*
#
# Olivier Locard

import pytest

from restapicall.api import ApiCall


@pytest.fixture
def api_call():
    return ApiCall


class TestApiCall:
    assert isinstance(ApiCall, object) is True
    assert str(ApiCall(endpoint='http://example.org')) == "{'endpoint': 'http://example.org', 'uri': (), 'args': {}}"


def test_get(api_call):
    assert api_call('http://example.org/').get().status_code == 200
