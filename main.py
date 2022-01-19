import sys
import pickle

GENE_LIST_PKL=sys.argv[1]
SFARI_PKL=sys.argv[2]

dict_main = {} # main data collection
with open(GENE_LIST_PKL, 'rb') as f:
	dict_main = pickle.load(f)

with open(SFARI_PKL, 'rb') as f:
	dict_SFARI = pickle.load(f)
	for gene in dict_main:
		if gene in dict_SFARI:
			dict_main[gene]['Source'] += "SFARI, "
			dict_main[gene].update(dict_SFARI[gene])
print(dict_main)
