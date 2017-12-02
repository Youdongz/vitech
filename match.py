import json
import urllib2

i = 0
with open('basic_10000.json', 'r') as f:
	docs = json.load(f)

	ids = []
	with open('details_10000.json', 'a') as d:
		d.write("[")
		with open('decisions_10000.json', 'a') as p:
			p.write("[")
			for doc in docs:
				ids.append(doc['id'])
				print i, doc['id']
				i +=1
				query = "https://v3v10.vitechinc.com/solr/v_participant_detail/select?indent=on&wt=json&q=id:" + doc['id']
				response = urllib2.urlopen(query).read()
				deet = json.loads(response)['response']['docs'][0]
				d.write(json.dumps(deet, indent=4) + ",")

				query = "https://v3v10.vitechinc.com/solr/v_quotes/select?indent=on&wt=json&q=id:" + doc['id']
				response = urllib2.urlopen(query).read()
				decision = json.loads(response)['response']['docs'][0]
				p.write(json.dumps(decision, indent=4) + ",")
			p.write("]")
		d.write("]")