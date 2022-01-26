import sys
import pickle
import os
import pandas as pd
import numpy as np

OUTDIR=sys.argv[1]
dict_main = {} # main data collection

# Gene List Provided
with open(os.path.join(OUTDIR, 'dict_genes.pickle'), 'rb') as f:
	dict_main = pickle.load(f)

# SFARI =========================================
with open(os.path.join(OUTDIR, 'dict_SFARI.pickle'), 'rb') as f:
	dict_SFARI = pickle.load(f)
	for gene in dict_main:
		if gene in dict_SFARI:
			dict_main[gene]['Source'] += "SFARI | "
			dict_main[gene].update(dict_SFARI[gene])

# DIOPT =========================================
#df_fly = pd.read_csv(os.path.join(os.path.join(OUTDIR,'ingested_data'),'df_fly.csv'),sep='\t')
#df_yeast = pd.read_csv(os.path.join(os.path.join(OUTDIR,'ingested_data'),'df_yeast.csv'),sep='\t')
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
    for index, row in df_fly.loc[df_fly['human_symbol'] == gene].iterrows():
        if 'HGNC' not in dict_main[gene]:
            dict_main[gene]['HGNC'] = row['HGNC']
        if row['score'] > fly_score:
            fly_symb = row['symbol2']
            fly_score = row['score']
            fly_id = row['species_specific_id2']
        if row['best_score'] == 'Yes' and row['best_score_rev'] == 'Yes' and row['confidence'] == 'high':
            best_fly_orth = True
    ### yeast
    yeast_score = 0
    yeast_symb = ''
    yeast_id = ''
    best_yeast_orth = False
    for index, row in df_yeast.loc[df_yeast['human_symbol'] == gene].iterrows():
        if 'HGNC' not in dict_main[gene]:
            dict_main[gene]['HGNC'] = row['HGNC']
        if row['score'] > yeast_score:
            yeast_symb = row['symbol2']
            yeast_score = row['score']
            yeast_id = row['species_specific_id2']
        if row['best_score'] == 'Yes' and row['best_score_rev'] == 'Yes' and row['confidence'] == 'high':
            best_yeast_orth = True

    # Add to main
    dict_main[gene]['Best DIOPT Score (Fly)'] = fly_score
    dict_main[gene]['Symbol (Fly)'] = fly_symb
    dict_main[gene]['Flybase ID'] = fly_id
    dict_main[gene]['Best Ortholog (Fly)'] = best_fly_orth
    dict_main[gene]['Best DIOPT Score (Yeast)'] = yeast_score
    dict_main[gene]['Symbol (Yeast)'] = yeast_symb
    dict_main[gene]['SGD ID'] = yeast_id
    dict_main[gene]['Best Ortholog (Yeast)'] = best_yeast_orth

# ClinVar =======================================
with open(os.path.join(OUTDIR, 'dict_clinvar.pickle'), 'rb') as f:
	dict_clinvar = pickle.load(f)
	for gene in dict_main:
		if gene in dict_clinvar:
			dict_main[gene]['Source'] += "ClinVar | "
			# ClinVar counts
			dict_main[gene]['ClinVar: Pathogenic & Likely Pathogenic'] = 0
			dict_main[gene]['ClinVar: Benign & Likely Benign'] = 0
			dict_main[gene]['ClinVar: VUS'] = 0
			dict_main[gene]['ClinVar: Conflicting'] = 0
			for variant in dict_clinvar[gene]:
				if variant['CLNSIG'] in ['Benign', 'Likely_benign']:
					dict_main[gene]['ClinVar: Benign & Likely Benign'] += 1
				elif variant['CLNSIG'] in ['Pathogenic', 'Likely_pathogenic']:
					dict_main[gene]['ClinVar: Pathogenic & Likely Pathogenic'] += 1
				elif variant['CLNSIG'] == 'Uncertain_significance':
					dict_main[gene]['ClinVar: VUS'] += 1
				elif variant['CLNSIG'] == 'Conflicting_interpretations_of_pathogenicity':
					dict_main[gene]['ClinVar: Conflicting'] += 1
			# CLNDN?

# VariCarta

# Gene2PubMed

# GnomAD


# save main as dict
with open(os.path.join(OUTDIR,'dict_main.pickle'), 'wb') as f:
        pickle.dump(dict_main, f, protocol=pickle.HIGHEST_PROTOCOL)
