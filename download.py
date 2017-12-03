import urllib.request
import json

UNIT = 1482000

# url = 'https://v3v10.vitechinc.com/solr/v_participant/select?indent=on&q=*:*&wt=json&rows=%d' % UNIT
# print("Downloading...")
# response = urllib.request.urlopen(url)

# with open('basic_%d.json' % UNIT, 'ab') as f:
# 	data = response.read()
# 	f.write(data)

# print("Done.")

url = 'https://v3v10.vitechinc.com/solr/v_participant_detail/select?indent=on&q=*:*&wt=json&rows=%d' % UNIT
print("Downloading...")
response = urllib.request.urlopen(url)

with open('specific_%d.json' % UNIT, 'ab') as f:
	data = response.read()
	print("Writing data...")
	f.write(data)

print("Done.")


# url = 'https://v3v10.vitechinc.com/solr/v_quotes/select?indent=on&q=*:*&wt=json&rows=%d' % UNIT
# print("Downloading...")
# response = urllib.request.urlopen(url)

# with open('decision_%d.json' % UNIT, 'ab') as f:
# 	data = response.read()
# 	print("Writing data...")
# 	f.write(data)

print("Done.")
