import json

BRONZE = 'BRONZE'
SILVER = 'SILVER'
GOLD = 'GOLD'
PLATINUM = 'PLATINUM'

classes = {}
with open('decisions_10000.json', 'r') as f:
	data = json.load(f)
	for doc in data:
		key = doc[BRONZE] + " " + doc[SILVER] + doc[GOLD] + doc[PLATINUM]
		if key not in classes:
			classes[key] = 0

		classes[key] += 1
	print classes
