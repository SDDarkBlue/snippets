import requests
import re
from lxml import etree
from jinja2 import Environment, FileSystemLoader

class BlogParser():

    def fetch_all_articles(self, url):
        r = requests.get(url)
	return r.text

    def parse_entry(self, entry_as_xml):
        entry_as_dict = {}
	for child_element in entry_as_xml.iterchildren():
	    if re.search('title', child_element.tag) != None:
		entry_as_dict['title'] = child_element.text
	    elif re.search('content', child_element.tag) != None:
	        entry_as_dict['content'] = child_element.text
	    elif re.search('published at', child_element.tag) != None:
	        entry_as_dict['published_at'] = child_element.text
	return entry_as_dict

    def parse_feeds_result(self, inputxml):
        doc = etree.fromstring(inputxml)
	articles = []
	for child_element in doc.iterchildren():
	    if re.search('entry', child_element.tag) != None:
		articles.append(self.parse_entry(child_element))
	return articles

    def search_article(self, url, parameters):
        r = requests.get(url, params=parameters)
	return self.parse_feeds_result(r.text.encode('utf-8'))

