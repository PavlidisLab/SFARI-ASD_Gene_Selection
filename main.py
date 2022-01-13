import pickle
import os
import sys

DATA=sys.argv[1]

dict = {}

with open(os.path.join(DATA,"gene_list.txt"), 'r') as gene_list:
	for index, gene in enumerate(gene_list):
		dict[str(gene.strip())] = [index]








#save as dict
'''
with open('dictionary.pickle', 'wb') as f:
	pickle.dump(dict, f, protocol=pickle.HIGHEST_PROTOCOL)

with open('dictionary.pickle', 'rb') as f:
	a = pickle.load(f)
	print(type(a))
'''



