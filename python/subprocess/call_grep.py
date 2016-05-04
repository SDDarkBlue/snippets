#!/usr/bin/python
import subprocess

####
# create test file
####
outfile = file("test_grepfile.txt", "w+")
outfile.write("A thing worth doing is worth doing well.")
outfile.close()

# How do you run grep with subprocess?
subprocess.call("grep --color thing test_grepfile.txt", shell=True)

# How to retrieve the output?
grep_result = subprocess.check_output("grep thing test_grepfile.txt", shell=True)
print "I fetched: ", grep_result

# However, grep returns a non-zero exit code when no match was found. Therefore:
try:
    grep_result = subprocess.check_output("grep object test_grepfile.txt", shell=True)
    print "I fetched: ", grep_result
except subprocess.CalledProcessError as e:
    print "No 'object' was found. This gives exit code 1"
    print "the exitcode was: ", e.returncode
    print "the error message was: ", e.message
    print "the output was: ", e.output

# What does grep return when the file was not found?
print "\n\non to the next exercise"
try:
    grep_result = subprocess.check_output("grep object nonexistingfile.txt", stderr=subprocess.STDOUT, shell=True)
except subprocess.CalledProcessError as e:
    print "When a file is not found, the exit code is 2"
    print "the exitcode was: ", e.returncode
    print "the error message was: ", e.message
    print "the output was: ", e.output
