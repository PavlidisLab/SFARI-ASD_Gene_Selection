import sys
import pickle
import os
import pandas as pd
import numpy as np

OUTDIR=sys.argv[1]

with open(os.path.join(OUTDIR, 'dict_main.pickle'), 'rb') as f:
        dict_main = pickle.load(f)

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
            dict_main[gene]['ClinVar Phenotype'] = ''
            CLNDN = set()
            for variant in dict_clinvar[gene]:
                if variant['CLNSIG'] in ['Benign', 'Likely_benign']:
                    dict_main[gene]['ClinVar: Benign & Likely Benign'] += 1
                elif variant['CLNSIG'] in ['Pathogenic', 'Likely_pathogenic']:
                    dict_main[gene]['ClinVar: Pathogenic & Likely Pathogenic'] += 1
                elif variant['CLNSIG'] == 'Uncertain_significance':
                    dict_main[gene]['ClinVar: VUS'] += 1
                elif variant['CLNSIG'] == 'Conflicting_interpretations_of_pathogenicity':
                    dict_main[gene]['ClinVar: Conflicting'] += 1
                #CLNDN
                if '|' in str(variant['CLNDN']):
                    phenotypes = str(variant['CLNDN']).split('|')
                    for p in phenotypes:
                        if p != 'not_provided' and p != 'not_specified':
                            CLNDN.add(p)
                elif str(variant['CLNDN']) != 'not_provided' and str(variant['CLNDN']) != 'not_specified':
                    CLNDN.add(str(variant['CLNDN']))
            dict_main[gene]['ClinVar Phenotype'] = ', '.join([str(p) for p in CLNDN])

# save main as dict
with open(os.path.join(OUTDIR,'dict_main.pickle'), 'wb') as f:
        pickle.dump(dict_main, f, protocol=pickle.HIGHEST_PROTOCOL)
