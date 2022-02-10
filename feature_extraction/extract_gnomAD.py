import sys
import os
import pickle
import vcfpy
from datetime import datetime

print("Starting gnomAD variant ingestion...")
print("time: ", datetime.now())

OUTDIR=sys.argv[1]
VARIANTS_DIR=sys.argv[2]
GNOMAD=sys.argv[3]

reader = vcfpy.Reader.from_path(GNOMAD)
with open(os.path.join(OUTDIR, 'dict_main.pickle'), 'rb') as f:
    dict_main = pickle.load(f)
    for gene in dict_main:
        if "gnomAD" in dict_main[gene]['Source']:
            writer = vcfpy.Writer.from_path(os.path.join(VARIANTS_DIR,gene), reader.header)
            count = 0
            for record in reader.fetch(dict_main[gene]['Chromosome'],dict_main[gene]['Starting Pos'],dict_main[gene]['End Pos']):
                if 'AF' in record.INFO and record.INFO['AF'][0] > 0.0001:
                    count += 1
                    writer.write_record(record)
            dict_main[gene]['gnomAD Variant Count'] = count
            #if count == int(0.5*len(dict_main)):
                #print("50% done. Time: ", datetime.now())
    print("100% done. Time: ", datetime.now())

# save as dict
with open(os.path.join(OUTDIR,'dict_main.pickle'), 'wb') as f:
    pickle.dump(dict_main, f, protocol=pickle.HIGHEST_PROTOCOL)
