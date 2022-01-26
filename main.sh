#!/bin/bash
# This is the main program for the SFARI ASD Gene Selection/Prioritization porject, 
# Aim 1.1 from the Proposal Narrative.

# Script Info====================================
# ===============================================
readonly PROGNAME=$(basename ${BASH_SOURCE[0]});
readonly PROGDIR=$(readlink -m $(dirname ${BASH_SOURCE[0]}));

# Input Params===================================
# ===============================================
if [[ $# -lt 7 ]]; then
        #echo "Usage: $PROGNAME GENE_LIST DB1 DB2 [...]".
	echo "Usage: $PROGNAME <SFARI> <DIOPT> <GENE2PUBMED> <CLINVAR> <VARICARTA> <OUTDIR> <GENE LIST>"
	exit;
fi

readonly SFARI="$1"; shift;
#readonly -a DBS=("$@");
readonly DIOPT="$1"; shift;
readonly GENE2PUBMED="$1"; shift;
readonly CLINVAR="$1"; shift;
readonly VARICARTA="$1"; shift;
readonly OUTDIR="$1"; shift;
readonly GENE_LIST="$1"; shift;

# Main Pipeline==================================
# ===============================================
main () {
	# load required modules from Compute Canada
	source /cvmfs/soft.computecanada.ca/config/profile/bash.sh
	module load python/3.7.0;
	module load scipy-stack;

	# set-up environment
	#mkdir $OUTDIR/ingested_data

	# =======================================
	# Step 1: Data Ingestion via Database Files
	# =======================================

	### Gene List (.txt file)
	python3 $PROGDIR/data_ingestion/ingest-gene_list.py $OUTDIR $GENE_LIST

	### SFARI (.csv file)
	#bash $PROGDIR/utils/data-ingestion/ingest-SFARI.py $OUTDIR/ingested_data $SFARI
	python3 $PROGDIR/data_ingestion/ingest-SFARI.py $OUTDIR $SFARI

	### DIOPT
	#bash $PROGDIR/utils/data-ingestion/ingest-DIOPT.py $OUTDIR/ingested_data $DIOPT
	python3 $PROGDIR/data_ingestion/ingest-DIOPT.py $OUTDIR $DIOPT

	### ClinVar (.vcf.gz file)
	#bash $PROGDIR/utils/data-ingestion/ingest-clinvar.py $OUTDIR/ingested_data $CLINVAR
	python3 $PROGDIR/data_ingestion/ingest-clinvar.py $OUTDIR $CLINVAR

	### Gene2PubMed


	### VariCarta


	### gnomAD


	# =======================================
	# Step 2: Feature Extraction
	# =======================================

	### general features
	python3 $PROGDIR/feature_extraction/extract_general.py $OUTDIR

	### DIOPT features
	python3 $PROGDIR/feature_extraction/extract_DIOPT.py $OUTDIR $DIOPT

	### ClinVar features
	python3 $PROGDIR/feature_extraction/extract_clinvar.py $OUTDIR 

	### VariCarta


	### get CSV	
	python3 $PROGDIR/utils/get_main_csv.py $OUTDIR

} #main

main
