import pickle
import os
import sys
from datetime import datetime

OUTDIR=sys.argv[1]
GENE_LIST=sys.argv[2]

print("starting gene list data ingestion...")
print("Time: ",datetime.now())

dict_genes = {}

with open(GENE_LIST, 'r') as gene_list:
    for index, gene in enumerate(gene_list):
        dict_genes[str(gene.strip())] = {}
        dict_genes[str(gene.strip())]['Source'] = ""

print(dict_genes)
#save as dict
with open(os.path.join(OUTDIR,'dict_genes.pickle'), 'wb') as f:
	pickle.dump(dict_genes, f, protocol=pickle.HIGHEST_PROTOCOL)

print("done.")
print("time: ", datetime.now())

