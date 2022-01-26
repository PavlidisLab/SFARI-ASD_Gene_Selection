import sys
import pickle
import os
import pandas as pd
import numpy as np

OUTDIR=sys.argv[1]
dict_main = {} # main data collection

# Gene List Provided
with open(os.path.join(OUTDIR, 'dict_genes.pickle'), 'rb') as f:
	dict_main = pickle.load(f)

# SFARI =========================================
with open(os.path.join(OUTDIR, 'dict_SFARI.pickle'), 'rb') as f:
	dict_SFARI = pickle.load(f)
	for gene in dict_main:
		if gene in dict_SFARI:
			dict_main[gene]['Source'] += "SFARI | "
			dict_main[gene].update(dict_SFARI[gene])

# save main as dict
with open(os.path.join(OUTDIR,'dict_main.pickle'), 'wb') as f:
        pickle.dump(dict_main, f, protocol=pickle.HIGHEST_PROTOCOL)
