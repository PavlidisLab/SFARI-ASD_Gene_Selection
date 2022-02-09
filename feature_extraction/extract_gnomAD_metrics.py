import os
import sys
import pickle
import pandas as pd
from datetime import datetime

OUTDIR=sys.argv[1]
gnomAD_metrics=sys.argv[2]
#gnomAD_VCF=sys.argv[3]

print("starting gnomAD processes...")
print("time: ", datetime.now())

df_metrics = pd.read_csv(gnomAD_metrics, compression='gzip', header=0, sep='\t')
#print(df_m.head())

# Fields of Interest
fields = [  'gene',
            #'transcript',
            'chromosome',
            'start_position',
            'end_position',
            'mis_z',
            'oe_mis',
            'oe_mis_lower',
            'oe_mis_upper',
            'pLI',
            'oe_lof',
            'oe_lof_lower',
            'oe_lof_upper']

df_m = df_metrics[fields]

with open(os.path.join(OUTDIR, 'dict_main.pickle'), 'rb') as f:
    dict_main = pickle.load(f)

    for index, row in df_m.iterrows():
        if row['gene'] in dict_main:
            dict_main[row['gene']]['Source'] += 'gnomAD | '
            dict_main[row['gene']]['Chromosome'] = row['chromosome']
            dict_main[row['gene']]['Starting Pos'] = row['start_position']
            dict_main[row['gene']]['End Pos'] = row['end_position']
            dict_main[row['gene']]['mis_z'] = row['mis_z']
            dict_main[row['gene']]['oe_mis'] = row['oe_mis']
            dict_main[row['gene']]['oe_mis_lower'] = row['oe_mis_lower']
            dict_main[row['gene']]['oe_mis_upper'] = row['oe_mis_upper']
            dict_main[row['gene']]['pLI'] = row['pLI']
            dict_main[row['gene']]['oe_lof'] = row['oe_lof']
            dict_main[row['gene']]['oe_lof_lower'] = row['oe_lof_lower']
            dict_main[row['gene']]['oe_lof_upper'] = row['oe_lof_upper']

# save main as dict
with open(os.path.join(OUTDIR,'dict_main.pickle'), 'wb') as f:
        pickle.dump(dict_main, f, protocol=pickle.HIGHEST_PROTOCOL)

