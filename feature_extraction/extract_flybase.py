import sys
import os
import pandas as pd
import pickle

OUTDIR=sys.argv[1]

with open(os.path.join(OUTDIR, 'dict_main.pickle'), 'rb') as f, open(os.path.join(OUTDIR, 'dict_fb.pickle'), 'rb') as g:
    dict_main = pickle.load(f)
    dict_fb = pickle.load(g)
    for gene in dict_main:
        if dict_main[gene]['Flybase ID'] in dict_fb:
            dict_main[gene].update(dict_fb[dict_main[gene]['Flybase ID']])
        else:
            dict_main[gene]['Flybase Snapshot'] = None
            dict_main[gene]['Flybase datestamp'] = None
            dict_main[gene]['Flybase: Gene Summary'] = None


'''
df_fb = pd.read_csv(os.path.join(OUTDIR,'df_fb.csv'), header=0, sep='\t')
df_main = pd.read_csv(os.path.join(OUTDIR,'main.csv'), header=0, sep='\t')
main = pd.merge(df_fb, df_main, on='Flybase ID')

main.to_csv(os.path.join(OUTDIR,'main.csv'), sep='\t')
'''
# save main as dict
with open(os.path.join(OUTDIR,'dict_main.pickle'), 'wb') as f:
    pickle.dump(dict_main, f, protocol=pickle.HIGHEST_PROTOCOL)

