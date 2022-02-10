import sys
import pickle
import os

OUTDIR=sys.argv[1]

with open(os.path.join(OUTDIR, 'dict_main.pickle'), 'rb') as f:
    dict_main = pickle.load(f)
    for gene in dict_main:
        dict_main[gene]['Gene Ontology'] = "http://amigo.geneontology.org/amigo/gene_product/UniProtKB:" + str(dict_main[gene]['UniProt ID'])

# save main as dict
with open(os.path.join(OUTDIR,'dict_main.pickle'), 'wb') as f:
    pickle.dump(dict_main, f, protocol=pickle.HIGHEST_PROTOCOL)

