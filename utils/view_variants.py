import pickle
import sys

FILE=sys.argv[1] #pickle file
GENE=sys.argv[2] #gene of interest

with open(FILE, 'rb') as f:
    d = pickle.load(f)
    #print(d)
    print(d['PHB1'])
    for var in d[str(GENE)]:
        print(var)

