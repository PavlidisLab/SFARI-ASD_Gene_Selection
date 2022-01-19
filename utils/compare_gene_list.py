import sys


FILE_A=sys.argv[1]
FILE_B=sys.argv[2]

with open(FILE_A,'r') as A, open(FILE_B,'r') as B:
	genes_A = A.readlines()
	genes_A = [gene.rstrip() for gene in genes_A]

	genes_B = B.readlines()
	genes_B = [gene.rstrip() for gene in genes_B]

a = set(genes_A)
b = set(genes_B)

print("Union: ", len(a|b))
print("Overlap: ", len(a&b))
print("in new, not in og: ", len(a-b))
print(a-b)
print("in og, not in new: ", len(b-a))
print(b-a)
#print("Difference: ", len((a-b)|(b-a)))
#print((a-b)|(b-a))
