import pandas as pd

with open('basic.json', 'r') as f:
	data = f.read()
	json = json.load(f)
	df = pd.DataFrame.from_dict(json)
	randomized = df.sample(frac=1).reset_index(drop=True)
	pd.DataFrame.to_json("shuffled_basic.json")

with open("shuffled_basic.json", 'r') as f:
	data = f.read()
	print data