# -- coding: utf-8 --
import urllib2
import urlparse
from urlparse import urljoin
from HTMLParser import HTMLParser

links = set()

class MyHTMLParser(HTMLParser):

    def handle_starttag(self, tag, attrs):
    	base_url = 'http://en.wikipedia.org/'
        if tag != 'a':
            return
        for attribute, value in attrs:
        	if attribute == 'href':
        		url = urljoin(base_url,value)
        		links.add(url)

class Web_crawl(): 

	def extract_url(self,cur_url):

		try:
			f = urllib2.urlopen(cur_url)
			html = f.read()
		except urllib2.HTTPError as e:
			return []

		html = html.decode('utf-8')
		parser = MyHTMLParser()
		parser.feed(html)

		new_res = []
		for l in links:
			new_res.append(l)
		return new_res


	def crawlbfs(self,url):
		queue  = []
		result = set()
		queue.append(url)

		while queue:
			cur = queue.pop(0)
			print(cur)
			cur_children = self.extract_url(cur)

			if len(cur_children) != 0:
				for nxt in cur_children:
					if nxt not in result:
							queue.append(nxt)
							result.add(nxt)
		return result

print(Web_crawl().crawlbfs('https://commons.wikimedia.org/wiki/Main_Page')) 	
