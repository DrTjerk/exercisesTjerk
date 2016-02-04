# Note - this code must run in Python 2.x and you must download
# http://www.pythonlearn.com/code/BeautifulSoup.py
# Into the same folder as this program

import urllib
from BeautifulSoup import *

url = raw_input('Enter - ')
html = urllib.urlopen(url).read()

soup = BeautifulSoup(html)

# Retrieve all of the anchor tags
tags = soup('span')
count = 0
for tag in tags:
    # Look at the parts of a tag
    #print 'SPAN:',tag
    #print 'is there something in span:',tag.get('span', None)
    #print 'Number:',tag.contents[0]
    #print 'Total Count: ', count
    i = int(tag.contents[0])
    count = count + i
    #print 'count: ',count
    #count = count + int(tag.contens[0])
    #print 'Span:',tags.attrs
print '=========================='
print 'count: ',count
print '=========================='
