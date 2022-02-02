import sys
import os
import pandas as pd
import pickle
from datetime import datetime

OUTDIR=sys.argv[1]
GENE2PUBMED=sys.argv[2]

print("starting Gene2PubMed data ingestion...")
print("time: ", datetime.now())

def get_pubcount(tax_id, gene_id, df):
    '''
    @params:
    tax_id      : taxonomy ID (e.g. 9606)
    gene_id     : NCBI Entrez ID (e.g. 4627 for MYH9)
    df          : Unzipped dataframe for Gene2PubMed database
    '''
    df_ = df.loc[(df['#tax_id'].astype(int) == tax_id) & (df['GeneID'].astype(int) == gene_id)]
    return df_['PubMed_ID'].unique()

df = pd.read_csv(GENE2PUBMED, header=0, sep='\t')
# Sample Usage: 
#print("Count for MYH9 (human) is: ", len(get_pubcount(9606, 4627, df)))

with open(os.path.join(OUTDIR, 'dict_main.pickle'), 'rb') as f:
    dict_main = pickle.load(f)
    df = df.loc[(df['#tax_id'].astype(int) == 9606)]
    for gene in dict_main:
        #if dict_main[gene]['NCBI Entrez ID'] in <gene2pubmed df>:
        publications = df.loc[(df['GeneID'].astype(int) == int(dict_main[gene]['NCBI Entrez ID']))]['PubMed_ID'].astype(int).unique()
        dict_main[gene]['Number of Publications (Gene2PubMed)'] = len(publications)

# Save main as dict
with open(os.path.join(OUTDIR,'dict_main.pickle'), 'wb') as f:
    pickle.dump(dict_main, f, protocol=pickle.HIGHEST_PROTOCOL)
