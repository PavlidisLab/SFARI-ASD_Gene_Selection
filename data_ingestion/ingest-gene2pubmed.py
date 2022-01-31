import sys
import os
import pandas as pd
#import csv

OUTDIR=sys.argv[1]
GENE2PUBMED=sys.argv[2]

def get_pubcount(tax_id, gene_id, df):
    '''
    usage e.g.
    print("Count for MYH9 (human) is: ", get_pubcount(9606, 7579, df))
    '''
    df_ = df.loc[(df['#tax_id'].astype(int) == tax_id) & (df['GeneID'].astype(int) == gene_id)]
    return df_['PubMed_ID'].unique()

df = pd.read_csv(GENE2PUBMED, header=0, sep='\t')
print("Count for MYH9 (human) is: ", len(get_pubcount(9606, 7579, df))) # wrong ID
print("List of Publications: ", get_pubcount(9606, 7579, df))

'''
dict_pubmedCount = {}

for tax_id in df['#tax_id'].astype(int).unique():
    dict_pubmedCount[tax_id] = {}
    genes = df.loc[(df['#tax_id'] == tax_id)]['GeneID'].astype(int).unique()
    for gene in genes:
        dict_pubmedCount[tax_id][gene] = get_pubcount(tax_id, gene, df)

print(dict_pubmedCount[9606])
'''
