from django.test import TestCase


class CoreTestCase(TestCase):
    def test_simple(self):
        assert 1 == 1
