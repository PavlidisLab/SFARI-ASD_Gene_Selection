#!/bin/bash

# Script info.
readonly PROGNAME=$(basename ${BASH_SOURCE[0]});
readonly PROGDIR=$(readlink -m $(dirname ${BASH_SOURCE[0]}));

exec ${PROGDIR}/main.sh \
 ${PROGDIR}/../../results/SFARI-ASD_Gene_Selection-out/ \
 /cosmos/data/project-data/SFARI-ASD_Gene_Selection-data/gene_list.txt \
 /cosmos/data/project-data/SFARI-ASD_Gene_Selection-data/hgnc_complete_set.txt \
 /cosmos/data/project-data/SFARI-ASD_Gene_Selection-data/SFARI-Gene_genes_09-02-2021release_01-12-2022export.csv \
 /cosmos/data/project-data/SFARI-ASD_Gene_Selection-data/DIOPTvs8_export20220131.zip \
 /cosmos/data/project-data/SFARI-ASD_Gene_Selection-data/clinvar_2021.vcf.gz \
 /cosmos/data/project-data/SFARI-ASD_Gene_Selection-data/gene2pubmed_20211210 \
 /cosmos/data/project-data/SFARI-ASD_Gene_Selection-data/VariCarta_export20220127.tsv \
 /cosmos/data/downloaded-data/gnomAD/2.1.1/gnomad.v2.1.1.lof_metrics.by_gene.txt.bgz \
 /cosmos/data/downloaded-data/gnomAD/2.1.1/gnomad.exomes.r2.1.1.sites.vcf.bgz \
 /cosmos/data/project-data/SFARI-ASD_Gene_Selection-data/flybase_bulk/ftp.flybase.net/releases/FB2021_06/precomputed_files/genes
