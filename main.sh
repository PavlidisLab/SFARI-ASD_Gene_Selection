#!/bin/bash
# This is the main program for the SFARI ASD Gene Selection/Prioritization porject, 
# Aim 1.1 from the Proposal Narrative.

# Script Info====================================
# ===============================================
readonly PROGNAME=$(basename ${BASH_SOURCE[0]});
readonly PROGDIR=$(readlink -m $(dirname ${BASH_SOURCE[0]}));

# Input Params===================================
# ===============================================
if [[ $# -lt 6 ]]; then
        #echo "Usage: $PROGNAME GENE_LIST DB1 DB2 [...]".
	echo "Usage: $PROGNAME <OUTDIR> <SFARI> <DIOPT> <GENE2PUBMED> <CLINVAR> <VARICARTA>"
	exit;
fi

readonly OUTDIR="$1"; shift;
readonly SFARI="$1"; shift;
#readonly -a DBS=("$@");
readonly DIOPT="$1"; shift;
readonly CLINVAR="$1"; shift;
readonly GENE2PUBMED="$1"; shift;
readonly VARICARTA="$1"; shift;


# Main Pipeline==================================
# ===============================================
main () {
	# load required modules from Compute Canada
	source /cvmfs/soft.computecanada.ca/config/profile/bash.sh
	module load python/3.7.0;
	module load scipy-stack;

	# set-up environment
	mkdir $OUTDIR/ingested_data

	# Step 1: Data Ingestion via Database Files
	
	### SFARI (.csv file)
	bash $PROGDIR/utils/data-ingestion/ingest-SFARI.py $OUTDIR/ingested_data $SFARI
	
	### DIOPT
	bash $PROGDIR/utils/data-ingestion/ingest-DIOPT.py $OUTDIR/ingested_data $DIOPT

	### ClinVar (.vcf.gz file)
	bash $PROGDIR/utils/data-ingestion/ingest-clinvar.py $OUTDIR/ingested_data $CLINVAR

	### Gene2PubMed


	### VariCarta


	# Step 2: Feature Extraction


} #main


