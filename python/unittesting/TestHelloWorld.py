import hello_classes
import unittest

class HelloWorldTestcase(unittest.TestCase):
    def test_HelloWorld(self):
	hw_object = hello_classes.HelloWorldClass()
	self.assertEqual("Hello World!", hw_object.getGreeting())
