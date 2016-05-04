#!/usr/bin/python

import json
import sys
import pandas as pd

if len(sys.argv) != 2:
    print "usage: ./readinfile.py <infile (in json)>"
    sys.exit(-1)

infile = sys.argv[1]
records = [json.loads(line) for line in open(infile)]
print "%s records found" % (len(records))
frame = pd.DataFrame(records)
print "dataframe: "
print frame
frame["waarde"].plot(kind="barh", rot=0)
