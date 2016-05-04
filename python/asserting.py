#!/usr/bin/python

def returnHi():
    return "hi"

assert returnHi() == "hi", "darn, the method did not return hi."
# make sure this test fails:
assert returnHi() != "hi", "ok, this test fails, because the method returns hi"
