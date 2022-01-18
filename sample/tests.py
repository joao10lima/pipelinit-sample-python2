from django.test import TestCase


class SampleTests(TestCase):
    def test_right(self):
        self.assertEquals(1 + 1, 2)

    def test_wrong(self):
        self.assertNotEquals(1 + 1, 3)
