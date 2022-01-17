import pickle
import sys

FILE=sys.argv[1] #pickle file

with open(FILE, 'rb') as f:
    d = pickle.load(f)
    print(d)
