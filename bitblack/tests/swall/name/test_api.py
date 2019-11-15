from unittest import TestCase
from bitblack.swall.samples.name import api


class TestApi(TestCase):
    def test_get_name(self):
        print(api.get_name())
