import sys
import os
import pickle

OUTDIR=sys.argv[1]

with open(os.path.join(OUTDIR, 'dict_HGNC.pickle'), 'rb') as f, open(os.path.join(OUTDIR, 'dict_main.pickle'), 'rb') as m:
    dict_HGNC = pickle.load(f)
    dict_main = pickle.load(m)
    for gene in dict_main:
        if gene in dict_HGNC:
            dict_main[gene].update(dict_HGNC[gene])

# save main as dict
with open(os.path.join(OUTDIR,'dict_main.pickle'), 'wb') as f:
    pickle.dump(dict_main, f, protocol=pickle.HIGHEST_PROTOCOL)
    
