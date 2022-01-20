import sys
import pickle
import os

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
