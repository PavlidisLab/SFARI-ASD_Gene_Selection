import pickle
import sys
import csv
import itertools
import os

OUTDIR=sys.argv[1]
#PKL=sys.argv[2] #pickle file

with open(os.path.join(OUTDIR,'dict_main.pickle'), 'rb') as f, open(os.path.join(OUTDIR,"main.csv"),'w') as g:
    d = pickle.load(f)
    #print(d.type())
    headers = ['Gene Symbol']
    headers.extend(list(d[list(d.keys())[0]].keys()))
    
    # if ordered
    '''
    headers = [ #general
                'Gene Symbol', 
                'HGNC', 
	            'Source', 
			    'SFARI Score',
                
                #DIOPT-Fly
			    'Best DIOPT Score (Fly)', 
			    'Symbol (Fly)',
                'Flybase ID', 
			    'Best Ortholog (Fly)', 
                
                #DIOPT-Yeast
			    'Best DIOPT Score (Yeast)', 
			    'Symbol (Yeast)',
                'SGD ID',
			    'Best Ortholog (Yeast)',
                
                #Depth of Conservation (via DIOPT)
                'Depth of Conservations (8 species total)', 

                #ClinVar
			    'ClinVar: Pathogenic & Likely Pathogenic', 
			    'ClinVar: Benign & Likely Benign', 
			    'ClinVar: VUS', 
			    'ClinVar: Conflicting'

		] #list of column fields wanted
        '''

    w = csv.DictWriter( g, fieldnames=headers, delimiter='\t')
    w.writeheader()
    for key, val in d.items():
        row = {'Gene Symbol': key}
        row.update(val)
        w.writerow(row)
	
