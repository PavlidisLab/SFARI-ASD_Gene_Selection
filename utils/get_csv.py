import pickle
import sys
import csv
import itertools
import os

OUTDIR=sys.argv[1]
PKL=sys.argv[2] #pickle file

with open(PKL, 'rb') as f, open(os.path.join(OUTDIR,"main.csv"),'w') as g:
	d = pickle.load(f)
	#print(d)
	headers = ['gene', 'Source', 'SFARI_score'] #list of column fields wanted

	w = csv.DictWriter( g, fieldnames=headers)
	w.writeheader()
	for key, val in d.items():
		row = {'gene': key}
		row.update(val)
		w.writerow(row)
	
