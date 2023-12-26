from files import func
import unittest


class FuncTests(unittest.TestCase):
    def test_success(self):
        self.assertTrue(func(2,10,'/Users/Sergei/Documents/GitHub/learning/files/'))

    def test_fail(self):
        self.assertFalse(func(2,11,'/Users/Sergei/Documents/GitHub/learning/files/'))
