from BeautifulSoup import *
import urllib2
import sys

# Strings
page = "http://giaitri.vnexpress.net/tin-tuc/gioi-sao/quoc-te/nguoi-dep-phap-dang-quang-hoa-hau-hoan-vu-2016-3534547.html"

# Request to page
content = urllib2.urlopen(page)

# Get links
soup = BeautifulSoup(content.read())
links = soup('img')

# Print it out
for link in links:
	print link.get('src')

