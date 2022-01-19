import pickle
import sys
import os

OUTDIR=sys.argv[1]
FILE=sys.argv[2] #pickle file

with open(os.path.join(OUTDIR,FILE), 'rb') as f, open(os.path.join(OUTDIR,"gene_list.txt"), 'w') as g:
	d = pickle.load(f)
	for gene in d:
		g.write(str(gene)+'\n')
