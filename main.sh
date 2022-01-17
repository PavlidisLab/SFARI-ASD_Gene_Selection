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
	echo "Usage: $PROGNAME GENE_LIST <DIOPT> <GENE2PUBMED> <CLINVAR> <VARICARTA> <OUTPUT DIR>"
	exit;
fi

readonly GENE_LIST="$1"; shift;
#readonly -a DBS=("$@");
readonly CLINVAR="$1"; shift;
readonly GENE2PUBMED="$1"; shift;
readonly DIOPT="$1"; shift;
readonly VARICARTA="$1"; shift;
readonly OUTDIR="$1"; shift;


# Main Pipeline==================================
# ===============================================
main () {


} #main


