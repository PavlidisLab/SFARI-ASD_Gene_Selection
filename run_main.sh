#!/bin/bash

# Script info.
readonly PROGNAME=$(basename ${BASH_SOURCE[0]});
readonly PROGDIR=$(readlink -m $(dirname ${BASH_SOURCE[0]}));
readonly DATADIR=/cosmos/data/project-data/SFARI-ASD_Gene_Selection-data

exec ${PROGDIR}/main.sh \
 ../SFARI-ASD_Variants/results/SFARI-ASD_Gene_Selection-out/ \
 $DATADIR/gene_list.txt \
 $DATADIR/hgnc_complete_set.txt \
 $DATADIR/SFARI-Gene_genes_09-02-2021release_01-12-2022export.csv \
 $DATADIR/DIOPTvs8_export20220131.zip \
 $DATADIR/clinvar_2021.vcf.gz \
 $DATADIR/gene2pubmed_20211210 \
 $DATADIR/VariCarta_export20220127.tsv \
 /cosmos/data/downloaded-data/gnomAD/2.1.1/gnomad.v2.1.1.lof_metrics.by_gene.txt.bgz \
 /cosmos/data/downloaded-data/gnomAD/2.1.1/gnomad.exomes.r2.1.1.sites.vcf.bgz \
 $DATADIR/flybase_bulk/ftp.flybase.net/releases/FB2021_06/precomputed_files/genes
