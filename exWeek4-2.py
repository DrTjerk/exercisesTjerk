# Note - this code must run in Python 2.x and you must download
# http://www.pythonlearn.com/code/BeautifulSoup.py
# Into the same folder as this program

import urllib
from BeautifulSoup import *

url = raw_input('Enter - ')
count = raw_input('Enter Count - ')
position = raw_input('Enter Position - ')

for x in range(0, int(count)):
    #print'nr: ', x
    html = urllib.urlopen(url).read()
    soup = BeautifulSoup(html)
    tags = soup('a')
    urlitem = tags[(int(position))-1]
    #print 'urlitem: ', urlitem
    print '============================================='
    print 'Retrieving URL: ', urlitem.get('href', None)
    print 'Name: ', urlitem.contents[0]
    print '============================================='
    url = urlitem.get('href', None)
#for tag in tags:
    # Look at the parts of a tag
    #print 'ahref:',tag
    #print 'is there something in span:',tag.get('span', None)
#    print 'Name:',tag.contents[0]
    #print 'Span:',tags.attrs
