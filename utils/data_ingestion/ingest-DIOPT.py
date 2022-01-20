import os
import sys
import pickle
import pandas as pd


#OUTDIR=sys.argv[1]
DIOPT=sys.argv[2]

df = pd.read_csv(DIOPT, compression='zip', header=0, sep='\t')
#print(df.head())
df_fly = df.loc[df['tax_id2'] == 7227]
df_yeast = df.loc[df['tax_id2'] == 4932]
print(df_fly.head())
print(df_yeast.head())

