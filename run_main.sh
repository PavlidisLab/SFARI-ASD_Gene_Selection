#!/bin/bash

# Script info.
readonly PROGNAME=$(basename ${BASH_SOURCE[0]});
readonly PROGDIR=$(readlink -m $(dirname ${BASH_SOURCE[0]}));

bash ${PROGDIR}/main.sh \
 ${PROGDIR}/../../results/SFARI-ASD_Gene_Selection-out/ \
 /cosmos/data/project-data/SFARI-ASD_Gene_Selection-data/gene_list.txt \
 /cosmos/data/project-data/SFARI-ASD_Gene_Selection-data/hgnc_complete_set.txt \
 /cosmos/data/project-data/SFARI-ASD_Gene_Selection-data/SFARI-Gene_genes_09-02-2021release_01-12-2022export.csv \
 /cosmos/data/project-data/SFARI-ASD_Gene_Selection-data/DIOPTvs8_export20220131.zip \
 /cosmos/data/project-data/SFARI-ASD_Gene_Selection-data/clinvar_2021.vcf.gz \
 /cosmos/data/project-data/SFARI-ASD_Gene_Selection-data/gene2pubmed_20211210 \
 /cosmos/data/project-data/SFARI-ASD_Gene_Selection-data/VariCarta_export20220127.tsv 

