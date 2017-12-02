import urllib2
import json

UNIT = 10000

url = 'https://v3v10.vitechinc.com/solr/v_participant/select?indent=on&q=*:*&wt=json&rows=%d' % UNIT
print "Downloading..."
response = urllib2.urlopen(url)

with open('data_%d.json' % UNIT, 'ab') as f:
	data = response.read()
	f.write(data)

print "Done."
