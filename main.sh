#!/bin/bash
# This is the main program for the SFARI ASD Gene Selection/Prioritization porject, 
# Aim 1.1 from the Proposal Narrative.

# Script Info====================================
# ===============================================
readonly PROGNAME=$(basename ${BASH_SOURCE[0]});
readonly PROGDIR=$(readlink -m $(dirname ${BASH_SOURCE[0]}));

# Input Params===================================
# ===============================================
if [[ $# -lt 10 ]]; then
        #echo "Usage: $PROGNAME OUTDIR GENE_LIST DB1 DB2 [...]".
    echo "Usage: $PROGNAME <OUTDIR> <GENE LIST> <HGNC> <SFARI> <DIOPT> <CLINVAR> <GENE2PUBMED> <VARICARTA> <GNOMAD METRICS> <GNOMAD EXOMES>"
    exit;
fi

#readonly INDIR="$1"; shift;
readonly OUTDIR="$1"; shift;
readonly GENE_LIST="$1"; shift;
readonly HGNC="$1"; shift;
readonly SFARI="$1"; shift;
readonly DIOPT="$1"; shift;
readonly CLINVAR="$1"; shift;
readonly GENE2PUBMED="$1"; shift;
readonly VARICARTA="$1"; shift;
readonly GNOMAD_METRICS="$1"; shift;
readonly GNOMAD="$1"; shift; #tbi assumed to be in same dir

# Main Pipeline==================================
# ===============================================
main () {
    # load required modules from Compute Canada
    #source /cvmfs/soft.computecanada.ca/config/profile/bash.sh
    #module load python/3.7.0;
    #module load scipy-stack;

    # download input files
    # Helper script available to help download most of the necessary files

    # =======================================
    # Step 1: Data Ingestion via Database Files
    # =======================================

    ### Gene List (.txt file)
    python3 $PROGDIR/data_ingestion/ingest-gene_list.py $OUTDIR $GENE_LIST

    ### Gene Names & IDs
    python3 $PROGDIR/data_ingestion/ingest-HGNC.py $OUTDIR $HGNC

    ### SFARI (.csv file)
    python3 $PROGDIR/data_ingestion/ingest-SFARI.py $OUTDIR $SFARI

    ### DIOPT
    python3 $PROGDIR/data_ingestion/ingest-DIOPT.py $OUTDIR $DIOPT

    ### ClinVar (.vcf.gz file)
    python3 $PROGDIR/data_ingestion/ingest-clinvar.py $OUTDIR $CLINVAR

    ### VariCarta
    python3 $PROGDIR/data_ingestion/ingest-varicarta.py $OUTDIR $VARICARTA

    ### gnomAD


    # =======================================
    # Step 2: Feature Extraction
    # =======================================

    ### general features
    python3 $PROGDIR/feature_extraction/extract_general.py $OUTDIR
    python3 $PROGDIR/feature_extraction/extract_HGNC.py $OUTDIR

    ### DIOPT features
    python3 $PROGDIR/feature_extraction/extract_DIOPT.py $OUTDIR $DIOPT

    ### ClinVar features
    python3 $PROGDIR/feature_extraction/extract_clinvar.py $OUTDIR 

    ### Gene2PubMed
    ### Features directly added to main data sheet
    python3 $PROGDIR/data_ingestion/ingest-gene2pubmed.py $OUTDIR $GENE2PUBMED

    ### VariCartaI
    python3 $PROGDIR/feature_extraction/extract_varicarta.py $OUTDIR

    ### gnomAD Metrics
    ### Features directly added to main data sheet
    python3 $PROGDIR/feature_extraction/extract_gnomAD_metrics.py $OUTDIR $GNOMAD_METRICS

    ### gnomAD Variants & Counts
    mkdir $OUTDIR/gnomAD_Variants
    python3 $PROGDIR/feature_extraction/extract_gnomAD.py $OUTDIR $OUTDIR/gnomAD_Variants $GNOMAD

    ### get CSV
    python3 $PROGDIR/utils/get_main_csv.py $OUTDIR

} #main

main
