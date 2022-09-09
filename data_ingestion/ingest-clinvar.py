import numpy as np
import pandas as pd
import gzip
import sys
import os
import pickle
from datetime import datetime

OUTDIR=sys.argv[1]
CLINVAR=sys.argv[2]

print("starting ClinVar data ingestion...")
print("time: ", datetime.now())

with gzip.open(CLINVAR, 'rt') as f:
    # skip comments
    for line in f:
        if line.startswith("#CHROM"):
              vcf_names = [x for x in line.split('\t')]
              break
    # specific to ClinVar
    vcf_names[0] = str(vcf_names[0])[1:] #CHROM
    vcf_names[-1] = str(vcf_names[-1])[:-1] #INFO
    vcf = pd.read_table(f, header=None, names=vcf_names, dtype={'CHROM': 'str'})

dict_clinvar = {}

#acceptable criteria for CLNREVSTAT
acceptable_status = [
        "criteria_provided,_single_submitter",
        "criteria_provided,_conflicting_interpretations",
        "criteria_provided,_multiple_submitters,_no_conflicts",
        "reviewed_by_expert_panel",
        "practice_guideline"]

for row in vcf.itertuples():
    info_dict = {}
    info = row[8].split(';')
    for i in info:
        info_dict[i.split('=')[0]] = i.split('=')[1]
    
    # filtering criteria
    if info_dict['CLNREVSTAT'] in acceptable_status:
        if info_dict['CLNVC'] == "single_nucleotide_variant":
            if ('MC' in info_dict) and (info_dict['MC'].split('|')[1] == "missense_variant"):
                # extracting gene info
                gene_symb = info_dict['GENEINFO'].split(':')[0]
                #info_dict['NCBI Entrez ID'] = info_dict['GENEINFO'].split(':')[1]
                #if '|' in info_dict['NCBI Entrez ID']:
                #    info_dict['NCBI Entrez ID'] = info_dict['NCBI Entrez ID'].split('|')[0]
                del info_dict['GENEINFO']
                
                # adding non-INFO properties
                info_dict['CHROM'] = row[1]
                info_dict['POS'] = row[2]
                info_dict['ID'] = row[3]
                info_dict['REF'] = row[4]
                info_dict['ALT'] = row[5]
                # collecting all variants of interest by gene
                if gene_symb not in dict_clinvar:
                    dict_clinvar[gene_symb] = []
                dict_clinvar[gene_symb].append(info_dict)

# save as dict
with open(os.path.join(OUTDIR,'dict_clinvar.pickle'), 'wb') as f:
    pickle.dump(dict_clinvar, f, protocol=pickle.HIGHEST_PROTOCOL)

#print("done @ ", datetime.now())

