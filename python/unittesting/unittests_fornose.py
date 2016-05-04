#!/usr/bin/python
import sys
import unittest

class TestClass(unittest.TestCase):
    def test_1(self):
        assert 1 == 1

    def test_2(self):
        assert 2 == 2
	pass

    def test_3(self):
        self.failUnless(3 == 3)

def testThis():
    a = 1
    b = 4
    assert a < b

