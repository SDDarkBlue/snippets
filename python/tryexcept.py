#!/usr/bin/python
def test():
    try:
        myfile = file("./thisfiledoesntexist.txt", "r")
    except IOError, e:
        print "the file doesn't exist, and I caught the exception"
	print "the error is --", e

test()
