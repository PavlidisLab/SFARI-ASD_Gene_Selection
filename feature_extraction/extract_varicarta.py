import sys
import pickle
import os
import pandas as pd
import numpy as np

OUTDIR=sys.argv[1]

with open(os.path.join(OUTDIR, 'dict_main.pickle'), 'rb') as f:
    dict_main = pickle.load(f)

with open(os.path.join(OUTDIR, 'dict_varicarta.pickle'), 'rb') as f:
    dict_vc = pickle.load(f)
    for gene in dict_main:
        if gene in dict_vc:
            dict_main[gene]['Source'] += "VariCarta | "
            dict_main[gene]['Number of De Novo (VariCarta)'] = len(dict_vc[gene]['De Novo'])
            dict_main[gene]['Number of Missense (VariCarta)'] = len(dict_vc[gene]['Missense'])

# save main as dict
with open(os.path.join(OUTDIR,'dict_main.pickle'), 'wb') as f:
    pickle.dump(dict_main, f, protocol=pickle.HIGHEST_PROTOCOL)
