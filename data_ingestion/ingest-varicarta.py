import os
import sys
import pickle
import pandas as pd
from datetime import datetime

OUTDIR=sys.argv[1]
VARICARTA=sys.argv[2]

print("starting VariCarta data ingestion...")
print("time: ", datetime.now())

df = pd.read_csv(VARICARTA, header=0, sep='\t')
df = df.loc[df['func'] == 'exonic'] # "Context" field on web
dict_vc = {}

for index, row in df.iterrows():
    gene_symbol = row['gene_symbol']
    if gene_symbol not in dict_vc:
        dict_vc[gene_symbol] = {}
        dict_vc[gene_symbol]['De Novo'] = {}
        dict_vc[gene_symbol]['Missense'] = {}
    # Differentiation of Entries: Criteria
    # Group by same sample ID AND Location AND REF/ALT
    tag = str(row['sample_id']) + ','
    tag += "chr" + str(row['chromosome']) + ':' + str(row['start_hg19']) + '-' + str(row['stop_hg19']) + ','
    tag += str(row['ref']) + ','
    tag += str(row['alt']) + ','
    
    # De Novo
    if str(row['inheritance']) == "d":
        if tag not in dict_vc[gene_symbol]['De Novo']:
            dict_vc[gene_symbol]['De Novo'][tag] = [] # row entry equivalent
        dict_vc[gene_symbol]['De Novo'][tag].append(row['paper_key'])
    if "nonsynonymous" in str(row['category']):
        if tag not in dict_vc[gene_symbol]['Missense']:
            dict_vc[gene_symbol]['Missense'][tag] = []
        dict_vc[gene_symbol]['Missense'][tag].append(row['paper_key'])

# save ingested db
with open(os.path.join(OUTDIR, 'dict_varicarta.pickle'), 'wb') as f:
    pickle.dump(dict_vc, f, protocol=pickle.HIGHEST_PROTOCOL)
