import json
import urllib2

with open('basic_10000.json', 'r') as f:
	details = []
	decisions = []
	docs = json.load(f)

	ids = []
	for doc in docs:
		ids.append(doc['id'])
		print doc['id']
		query = "https://v3v10.vitechinc.com/solr/v_participant_detail/select?indent=on&wt=json&q=id:" + doc['id']
		response = urllib2.urlopen(query)
		deet = response.read()
		details.append(deet)

		query = "https://v3v10.vitechinc.com/solr/v_quotes/select?indent=on&wt=json&q=id:" + doc['id']
		response = urllib2.urlopen(query)
		decision = response.read()
		decisions.append(decision)

	with open('details_10000.json', 'r') as d:
		d.write(details)

	with open('decisions_10000.json', 'r') as p:
		p.write(decisions)