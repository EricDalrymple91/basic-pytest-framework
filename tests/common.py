"""

"""
import pytest


class TestCommon(object):

    storage = {}

    @pytest.fixture()
    def number(self, pytestconfig):
        return int(pytestconfig.getoption('n'))

    @pytest.fixture()
    def text(self, pytestconfig):
        return pytestconfig.getoption('t')

    @pytest.fixture()
    def number_doubled(self, number):
        return number * 2
