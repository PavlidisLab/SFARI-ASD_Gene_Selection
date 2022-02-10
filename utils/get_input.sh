#!/bin/bash
# This script is for downloading publically available input files to the main pipeline.

# Script Info====================================
# ===============================================
readonly PROGNAME=$(basename ${BASH_SOURCE[0]});
readonly PROGDIR=$(readlink -m $(dirname ${BASH_SOURCE[0]}));

# Input Params===================================
# ===============================================
if [[ $# -lt 1 ]]; then
    echo "Usage: bash $PROGDIR/$PROGNAME <DIR>"
    exit;
fi

readonly INDIR="$1"; shift;

#HNGC
wget -O $INDIR/hgnc.tsv "http://ftp.ebi.ac.uk/pub/databases/genenames/hgnc/tsv/hgnc_complete_set.txt"


# SFARI
wget --no-check-certificate -O $INDIR/SFARI_export.csv "https://gene.sfari.org//wp-content/themes/sfari-gene/utilities/download-csv.php?api-endpoint=genes"

# VariCarta
wget -O $INDIR/VariCarta_export.tsv "https://varicarta.msl.ubc.ca/exports/export_latest.tsv"

# ClinVar
wget -O $INDIR/clinvar.vcf.gz "https://ftp.ncbi.nlm.nih.gov/pub/clinvar/vcf_GRCh37/clinvar.vcf.gz"

# GeneNames
wget -O $INDIR/genenames.tsv "http://ftp.ebi.ac.uk/pub/databases/genenames/hgnc/tsv/hgnc_complete_set.txt"

# Flybase
mkdir -p $INDIR/flybase_bulk
cd $INDIR/flybase_bulk
wget -r -np -R "index.html*" --recursive --no-parent "http://ftp.flybase.net/releases/FB2021_06/precomputed_files/"
cd $INDIR
tree -L 7



