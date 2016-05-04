#!/usr/bin/python
import subprocess
import sys

string, filename = sys.argv[1:]

try:
    process = subprocess.Popen(["fastq-grep", "-c", string, filename], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output = process.stdout.read()
    errors = process.stderr.read()
    if not output == "":
	print "no error occurred"
	print "I fetched: ", output.strip()
    elif errors == "":
        print "pattern not found"
    else:
	print "An error occurred. Probably file not found"
	print "standard output is: '{0}'".format(process.stdout.read())
	print "standard error is: '{0}'".format(process.stderr.read())
except subprocess.CalledProcessError as e:
    if e.returncode == 1:
	print "could not find the sequence in the file"
    elif e.returncode == 2:
        print "could not find file"
    else:
	print "something else went wrong"
	print e.output

