import sys
import pickle
import os

OUTDIR=sys.argv[1]
#GENE_LIST_PKL=sys.argv[2]
#SFARI_PKL=sys.argv[3]

dict_main = {} # main data collection
with open(os.path.join(OUTDIR, 'dict_genes.pickle'), 'rb') as f:
	dict_main = pickle.load(f)

with open(os.path.join(OUTDIR, 'dict_SFARI.pickle'), 'rb') as f:
	dict_SFARI = pickle.load(f)
	for gene in dict_main:
		if gene in dict_SFARI:
			dict_main[gene]['Source'] += "SFARI |"
			dict_main[gene].update(dict_SFARI[gene])


# save main as dict
with open(os.path.join(OUTDIR,'dict_main.pickle'), 'wb') as f:
        pickle.dump(dict_main, f, protocol=pickle.HIGHEST_PROTOCOL)
