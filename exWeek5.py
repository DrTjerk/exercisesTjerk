import urllib
import xml.etree.ElementTree as ET

serviceurl = 'http://maps.googleapis.com/maps/api/geocode/xml?'

#while True:
xml_address = raw_input('Enter location: ')
#    if len(xml_address) < 1 : break

    #url = serviceurl + urllib.urlencode({'sensor':'false', 'address': address})
print 'Retrieving', xml_address #url
uh = urllib.urlopen(xml_address)
data = uh.read()
print 'Retrieved',len(data),'characters'
    #print data
tree = ET.fromstring(data)

counts = tree.findall('.//count')
print len(counts)
counter = 0
for x in range (0, int(len(counts))):
    print 'Retrieved Number: ', counts[x].text
    counter = counter + int(counts[x].text)
    print 'Numbers Added up: ', counter

print '=============='
print 'Sum of numbers ', counter
