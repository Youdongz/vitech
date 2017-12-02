import urllib
import json

UNIT = 1400000

url = 'https://v3v10.vitechinc.com/solr/v_participant_detail/select?indent=on&q=*:*&wt=json&rows=%d' % UNIT
print ("Downloading...")
response = urllib.urlopen(url)

with open('specific_%d.json' % UNIT, 'ab') as f:
	data = response.read()
	f.write(data)

print ("Done.")
