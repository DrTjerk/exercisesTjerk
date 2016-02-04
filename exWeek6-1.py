import json
import urllib

serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?'

while True:
    url = raw_input('Enter - ')
    #address = raw_input('Enter location: ')
    if len(url) < 1 : break

    #url = serviceurl + urllib.urlencode({'sensor':'false', 'address': address})
    print 'Retrieving', url
    uh = urllib.urlopen(url)
    data = uh.read()
    print 'Retrieved',len(data),'characters'
    #print data

    try: js = json.loads(str(data))
    except: js = None
    if 'note' not in js:
           print '==== Failure To Retrieve ===='
           continue

    print json.dumps(js, indent=4)
    print 'length: ', len(js["comments"])
    totalCount = 0

    for x in range(0, len(js["comments"])):
        count = js["comments"][x]["count"]
        name = js["comments"][x]["name"]
        totalCount = totalCount + int(count)
        print 'Number: ', x, 'count: ',count,'name: ',name
    #location = js['results'][0]['formatted_address']
    print 'Total Count: ', totalCount


    #url = raw_input('Enter - ')
    #json = urllib.urlopen(url)
    #data = json.read(json)

    #print 'User count:', len(data), 'characters'

    #js = json.loads(str(data))
    #except: js = None
    #if 'status' not in js or js['status'] != 'OK':
    #    print '==== Failure To Retrieve ===='
    #    print data
        #continue

    #print json.dumps(js, indent=4)

    #for item in info:
        #print 'Name', item['name']
        #print 'Id', item['id']
        #print 'Attribute', item['x']
