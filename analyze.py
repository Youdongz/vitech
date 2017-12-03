import pandas as pd


with open('basic_decision_combined.json', 'r') as f:
	df = pd.DataFrame.from_records(f.read())
	print df