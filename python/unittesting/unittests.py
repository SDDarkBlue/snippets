#!/usr/bin/python
import unittest
import sys

class TestClass(unittest.TestCase):
    def test_1(self):
        assert 1 == 1

    def test_2(self):
        assert 2 == 2
	pass

    def test_3(self):
        self.failUnless(3 == 3)

def suite():
    loader = unittest.TestLoader()
    testsuite = loader.loadTestsFromTestCase(TestClass)
    return testsuite

def test():
    testsuite = suite()
    runner = unittest.TextTestRunner(sys.stdout, verbosity=2)
    result = runner.run(testsuite)

test()
