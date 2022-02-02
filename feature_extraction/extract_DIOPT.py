import sys
import pickle
import os
import pandas as pd
import numpy as np

OUTDIR=sys.argv[1]
DIOPT=sys.argv[2]

with open(os.path.join(OUTDIR, 'dict_main.pickle'), 'rb') as f:
        dict_main = pickle.load(f)

# DIOPT =========================================
df = pd.read_csv(DIOPT, compression='zip', header=0, sep='\t')
df_fly = pd.read_csv(os.path.join(OUTDIR,'df_fly.csv'),sep='\t')
df_yeast = pd.read_csv(os.path.join(OUTDIR,'df_yeast.csv'),sep='\t')
for gene in dict_main:
    dict_main[gene]['Source'] += "DIOPT | "
    # filtering criteria

    ### fly
    fly_score = 0
    fly_symb = ''
    fly_id = ''
    best_fly_orth = False
    fly_needle_id = None
    fly_needle_sim = None
    for index, row in df_fly.loc[df_fly['human_symbol'] == gene].iterrows():
        if 'HGNC' not in dict_main[gene]:
            dict_main[gene]['HGNC'] = row['HGNC']
        if row['score'] > fly_score:
            fly_symb = row['symbol2']
            fly_score = row['score']
            fly_id = row['species_specific_id2']
            fly_needle_id = row['align_identity']
            fly_needle_sim = row['align_similarity']
        if row['best_score'] == 'Yes' and row['best_score_rev'] == 'Yes' and row['confidence'] == 'high':
            best_fly_orth = True
    ### yeast
    yeast_score = 0
    yeast_symb = ''
    yeast_id = ''
    best_yeast_orth = False
    yeast_needle_id = None
    yeast_needle_sim = None
    for index, row in df_yeast.loc[df_yeast['human_symbol'] == gene].iterrows():
        if 'HGNC' not in dict_main[gene]:
            dict_main[gene]['HGNC'] = row['HGNC']
        if row['score'] > yeast_score:
            yeast_symb = row['symbol2']
            yeast_score = row['score']
            yeast_id = row['species_specific_id2']
            yeast_needle_id = row['align_identity']
            yeast_needle_sim = row['align_similarity']
        if row['best_score'] == 'Yes' and row['best_score_rev'] == 'Yes' and row['confidence'] == 'high':
            best_yeast_orth = True
    # depth of conservation
    dict_main[gene]['Depth of Conservations (8 species total)'] = len(df.loc[df['human_symbol'] == gene]['tax_id2'].unique())

    # Add to main
    dict_main[gene]['Best DIOPT Score (Fly)'] = fly_score
    dict_main[gene]['Symbol (Fly)'] = fly_symb
    dict_main[gene]['Flybase ID'] = fly_id
    dict_main[gene]['Best Ortholog (Fly)'] = best_fly_orth
    dict_main[gene]['Fly Alignment Similarity (%)'] = fly_needle_sim
    dict_main[gene]['Fly Alignment Identity (%)'] = fly_needle_id

    dict_main[gene]['Best DIOPT Score (Yeast)'] = yeast_score
    dict_main[gene]['Symbol (Yeast)'] = yeast_symb
    dict_main[gene]['SGD ID'] = yeast_id
    dict_main[gene]['Best Ortholog (Yeast)'] = best_yeast_orth
    dict_main[gene]['Yeast Alignment Similarity (%)'] = yeast_needle_sim
    dict_main[gene]['Yeast Alignment Identity (%)'] = yeast_needle_id

# save main as dict
with open(os.path.join(OUTDIR,'dict_main.pickle'), 'wb') as f:
        pickle.dump(dict_main, f, protocol=pickle.HIGHEST_PROTOCOL)
