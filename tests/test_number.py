"""

"""
from .common import TestCommon
import pytest


class TestNumber(TestCommon):

    @pytest.mark.number
    def test_number(self, number):
        assert isinstance(number, int)

    @pytest.mark.number
    @pytest.mark.skip('Simply a skip example')
    def test_double(self, number, number_doubled):
        assert number * 2 == number_doubled

    @pytest.mark.number
    @pytest.mark.dependency(name='test_storage1')
    def test_storage1(self, number):
        self.storage['number_plus1'] = number + 1
        assert self.storage['number_plus1'] > number

    @pytest.mark.number
    @pytest.mark.dependency(name='test_storage2', depends=['test_storage1'])
    def test_storage2(self, number):
        assert self.storage['number_plus1'] == number + 1

    @pytest.mark.number
    def test_number_too_big(self, number):
        assert number < 50

    @pytest.mark.number
    def test_number_too_small(self, number):
        assert number > 3
