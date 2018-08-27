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
    
def extract_url(cur_url):
    
	scr = urllib2.urlopen(cur_url)
	html = scr.read()

	parser = MyHTMLParser()
	parser.feed(html)

	new_res = []
	
	for l in links:
		new_res.append(l)
	return new_res

print(extract_url('http://en.wikipedia.org/')) 	
