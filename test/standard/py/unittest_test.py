# encoding: utf-8
import unittest as ut


class JustTest(ut.TestCase):
    def test_1(self):
        print('hello world')
        self.assertEqual(1, 2, 'error')
