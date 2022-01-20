import pickle
import sys
import csv
import itertools
import os

OUTDIR=sys.argv[1]
#PKL=sys.argv[2] #pickle file

with open(os.path.join(OUTDIR,'dict_main.pickle'), 'rb') as f, open(os.path.join(OUTDIR,"main.csv"),'w') as g:
	d = pickle.load(f)
	#print(d)
	headers = [	'Gene Symbol', 
			'Source', 
			'SFARI Score',
			'ClinVar: Pathogenic & Likely Pathogenic', 
			'ClinVar: Benign & Likely Benign', 
			'ClinVar: VUS', 
			'ClinVar: Conflicting'

		] #list of column fields wanted


	w = csv.DictWriter( g, fieldnames=headers)
	w.writeheader()
	for key, val in d.items():
		row = {'Gene Symbol': key}
		row.update(val)
		w.writerow(row)
	
