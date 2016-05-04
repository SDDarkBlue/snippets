#!/usr/bin/python
import csv
import sys

def checkarguments():
    if len(sys.argv) != 2:
	print "usage: ./tsv2json.py <infile>"
	sys.exit(-1)
    return sys.argv[1]

def transformHeaderToFields(header):
    header[0] = header[0].lstrip("#").strip()
    return header

def transformListToJson(list1, fields):
    json_dict = {}
    for i in range(len(list1)):
	json_dict[fields[i]] = list1[i]
    return str(json_dict).replace("\'", "\"")

def transform(input_filename):
    infile = file(input_filename)
    output = []
    reader = csv.reader(infile, delimiter="\t")
    header = reader.next()
    fields = transformHeaderToFields(header)
    for row in reader:
	jsonLine = transformListToJson(row, fields)
	output.append(jsonLine)
    return output

def printOutput(output):
    for row in output:
	print row

def main():
    input_filename = checkarguments()
    output = transform(input_filename)
    printOutput(output)

main()
