import sys
import pickle
import os
import gzip
import pandas as pd
from datetime import datetime

OUTDIR=sys.argv[1]
FBDIR=sys.argv[2]

print("starting Flybase ingestion...")
print("time: ", datetime.now())

# [Gene] Snapshot
fb_snapshot = pd.read_csv(os.path.join(FBDIR,'gene_snapshots_fb_2021_06.tsv.gz'), compression='gzip', skiprows=5, sep='\t', header=0)
fb_snapshot = fb_snapshot.rename(columns={"##FBgn_ID": 'Flybase ID'})
fb_snapshot = fb_snapshot.rename(columns={"datestamp": 'Flybase datestamp'})
fb_snapshot = fb_snapshot.rename(columns={"gene_snapshot_text": 'Flybase Snapshot'})
fb_snapshot = fb_snapshot.drop(['GeneSymbol', 'GeneName'], axis=1)

#print(fb_snapshot.head())

# [Gene] Summary
fb_summary = pd.read_csv(os.path.join(FBDIR,'automated_gene_summaries.tsv.gz'), compression='gzip', skiprows=2, sep='\t', header=None, names=['Flybase ID','Flybase: Gene Summary','NA'])
fb_summary = fb_summary.drop(['NA'], axis=1) #3rd NA column but header contains 2 fields
#print(fb_summary.head())

result = pd.merge(fb_snapshot, fb_summary, on='Flybase ID')
#print(result.head())

dict_fb = {}
for idx, row in result.iterrows():
    dict_fb[row['Flybase ID']] = {}
    dict_fb[row['Flybase ID']]['Flybase datestamp'] = row['Flybase datestamp']
    dict_fb[row['Flybase ID']]['Flybase Snapshot'] = row['Flybase Snapshot']
    dict_fb[row['Flybase ID']]['Flybase: Gene Summary'] = row['Flybase: Gene Summary']

#save merged df to csv
#result.to_csv(os.path.join(OUTDIR,'df_fb.csv'), sep='\t')

with open(os.path.join(OUTDIR,'dict_fb.pickle'), 'wb') as f:
    pickle.dump(dict_fb, f, protocol=pickle.HIGHEST_PROTOCOL)
