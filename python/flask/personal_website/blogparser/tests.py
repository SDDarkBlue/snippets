import blogparser
from nose.tools import assert_equals, assert_true
class TestBlogParser():
    def create_blogparser(self):
        self.bp = blogparser.BlogParser()

    def test_initialize(self):
        bp = blogparser.BlogParser()

    def test_fetch_article(self):
        self.create_blogparser()
        url = 'http://bioinformatics-man.blogspot.com/feeds/posts/default'
	assert_true(self.bp.fetch_all_articles(url) != '')

    def test_search_article(self):
        self.create_blogparser()
        url = 'http://bioinformatics-man.blogspot.com/feeds/posts/default'
	parameters = {'path': '/2012/11/what-is-bioinformatics-man.html'}
	assert_equals(self.bp.search_article(url, parameters)[0]['title'], 'What is bioinformatics-man?')
