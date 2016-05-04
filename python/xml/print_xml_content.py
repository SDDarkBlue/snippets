#!/usr/bin/python
from lxml import etree
doc = etree.parse("test.xml")
for element in doc.iterfind("taxon"):
    print element.find("name").text
