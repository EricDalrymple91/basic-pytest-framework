"""

"""
from .common import TestCommon
import pytest
import time


class TestText(TestCommon):

    @pytest.mark.text
    def test_text(self, text):
        assert isinstance(text, str)

    @pytest.mark.text
    def test_text_not_long(self, text):
        assert len(text) < 50

    @pytest.mark.text
    def test_text_not_short(self, text):
        assert len(text) > 3

    @pytest.mark.text
    @pytest.mark.timeout(2)
    def test_timeout(self, text):
        time.sleep(1)  # Set this to > 2 for it to fail
        assert isinstance(text, str)

