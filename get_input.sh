# download input files

#$INDIR=

# SFARI
wget --no-check-certificate -O $INDIR/SFARI_export.csv 'https://gene.sfari.org//wp-content/themes/sfari-gene/utilities/download-csv.php?api-endpoint=genes'

# VariCarta
wget -O $INDIR/VariCarta_export.tsv 'https://varicarta.msl.ubc.ca/exports/export_latest.tsv'

# ClinVar
wget -O $INDIR/clinvar.vcf.gz 'https://ftp.ncbi.nlm.nih.gov/pub/clinvar/vcf_GRCh37/clinvar.vcf.gz'

# GeneNames
wget -O $INDIR/genenames.tsv 'http://ftp.ebi.ac.uk/pub/databases/genenames/hgnc/tsv/hgnc_complete_set.txt'




