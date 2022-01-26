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
			'HGNC', 
			'Source', 
			'SFARI Score',
			'Best DIOPT Score (Fly)', 
			'Symbol (Fly)', 
			'Best Ortholog (Fly)', 
			'Best DIOPT Score (Yeast)', 
			'Symbol (Yeast)', 
			'Best Ortholog (Yeast)', 
			'ClinVar: Pathogenic & Likely Pathogenic', 
			'ClinVar: Benign & Likely Benign', 
			'ClinVar: VUS', 
			'ClinVar: Conflicting'

		] #list of column fields wanted


	w = csv.DictWriter( g, fieldnames=headers, delimiter='\t')
	w.writeheader()
	for key, val in d.items():
		row = {'Gene Symbol': key}
		row.update(val)
		w.writerow(row)
	
