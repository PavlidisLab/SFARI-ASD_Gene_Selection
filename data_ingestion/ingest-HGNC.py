import pandas as pd
import os
import sys
import pickle
from datetime import datetime

OUTDIR=sys.argv[1]
HGNC=sys.argv[2]

print("starting HGNC data ingestion...")
print("time: ", datetime.now())

df = pd.read_csv(HGNC, header=0, sep='\t')
#print(df.head())

df_HGNC = df[['symbol', 'name', 'alias_symbol','prev_symbol','entrez_id','ensembl_gene_id']]
#print(df_HGNC.head())

dict_hgnc = {}

for index, row in df_HGNC.iterrows():
    dict_hgnc[row['symbol']] = {}
    dict_hgnc[row['symbol']]['Gene Name'] = row['name']
    dict_hgnc[row['symbol']]['Prev Gene Symbol(s)'] = row['prev_symbol']
    dict_hgnc[row['symbol']]['NCBI Entrez ID'] = row['entrez_id']
    dict_hgnc[row['symbol']]['Ensembl ID'] = row['ensembl_gene_id']

# save main as dict
with open(os.path.join(OUTDIR,'dict_HGNC.pickle'), 'wb') as f:
    pickle.dump(dict_hgnc, f, protocol=pickle.HIGHEST_PROTOCOL)

