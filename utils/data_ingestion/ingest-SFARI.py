import pickle
import os
import sys
from datetime import datetime

OUTDIR=sys.argv[1]
SFARI=sys.argv[2]

print("starting SFARI gene data ingestion...")
print("Time: ",datetime.now())

dict_SFARI = {}

with open(SFARI, 'r') as SFARI_gene:
	for index, line in enumerate(SFARI_gene):
		if index == 0:
			continue
		line = str(line).split("\"")
		#print(len(line), line)
		syndr = str(line[-1].split(',')[2])
		score = str(line[-1].split(',')[1])

		#if score in ["1","2"] or syndr == "1":	
		gene_info = {}
		gene = line[0].split(',')[1]
		gene_info["SFARI Score"] = ""
		#print(gene, syndr, score)
		if score  == "1":
			gene_info["SFARI Score"] += "1"
		elif score == "2":
			gene_info["SFARI Score"] += "2"
		elif score == "3":
			gene_info["SFARI Score"] += "3"
		if syndr == "1":
			gene_info["SFARI Score"] += "S"
		#gene_info["Ensembl_id"] = line[2].split(',')[0]
		#gene_info["gene_name"] = line[1]
		#gene_info["chrom"] = line[2].split(',')[1]
		#gene_info["genetic_category"] = line[3]
		dict_SFARI[gene] = gene_info

#save as dict
with open(os.path.join(OUTDIR,'dict_SFARI.pickle'), 'wb') as f:
	pickle.dump(dict_SFARI, f, protocol=pickle.HIGHEST_PROTOCOL)

print("done.")
print("time: ", datetime.now())

