import json

BRONZE = "BRONZE"
SILVER = 'SILVER'
GOLD = 'GOLD'
PLATINUM = 'PLATINUM'

classes = {}
with open('decisions_10000.json', 'r') as f:
	data = json.load(f)
	for doc in data:
		total = sum([1 if BRONZE in doc else 0, 1 if SILVER in doc else 0, 1 if GOLD in doc else 0, 1 if PLATINUM in doc else 0])
		key = ((doc[BRONZE] if BRONZE in doc else 0) + doc[SILVER] + doc[GOLD] + doc[PLATINUM])/total
		print doc, key
		if key not in classes:
			classes[key] = 0

		classes[key] += 1

lst = [[key] + [classes[key]] for key in classes]
sort = sorted(lst, key=lambda k: k[0])
values = [each[1] for each in sort]
print sort
print values
