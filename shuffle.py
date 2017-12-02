import pandas as pd

with open('data.json', 'r') as f:
	json = json.load(f)
	df = pd.DataFrame.from_dict(json)
	randomized = df.sample(frac=1)