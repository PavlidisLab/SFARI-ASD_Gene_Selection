# [SFARI] ASD Gene Selection
ASD gene selection/prioritization pipeline for SFARI project. Ref Aim 1.1 in Project Proposal Narative. Reference genome hg19.

## Directories (DIR)
Overviews of important project DIRs listed in this section.
 
### Input (Data)
(sample file names provided as example)
├── `gene_list.txt`: list of gene symbols for data desired    
├── `SFARI-Gene_genes_09-02-2021release_01-12-2022export.csv`: SFARI Gene list, released 2021-09-02, obtained 2022-01-12 from https://gene.sfari.org//wp-content/themes/sfari-gene/utilities/download-csv.php?api-endpoint=genes    
├── `DIOPTvs8.zip` DIOPT version 8, obtained 2022-01-31 from author  
├── `clinvar_2021.vcf.gz`: ClinVar 2021 release, obtained 2022-01-13 from https://ftp.ncbi.nlm.nih.gov/pub/clinvar/   
├── `gene2pubmed_20211210`: Gene2PubMed 2021-12-10 release, obtained 2022-01-27   
├── `hgnc_complete_set.txt`: HGNC names obtained 2022-01-28 via https://www.genenames.org/download/archive/   
├── `VariCarta_export20220127.tsv`: VariCarta db obtained 2022-01-27 from https://varicarta.msl.ubc.ca/exports/export_latest.tsv   
├── `gnomad.v2.1.1.lof_metrics.by_gene.txt.bgz`: gnomAD metrics file
├── `gnomad.exomes.r2.1.1.sites.vcf.bgz`: gnomAD exomes vcf file (with tbi in same directory)
└── `/flybase_bulk`: Flybase Bulk Data Files obtained 2022-02-09 from https://wiki.flybase.org/wiki/FlyBase:Downloads_Overview#Drosophila_Data  

### Output (Results) DIR
/home/kchen/results/SFARI-ASD_Gene_Selection-out/  
├── `dict_<db>.pickle` where <db> is replaced by various database names   
├── `df_<db>.csv` where <db> is replaced by various database names  
├── `gnomAD_Variants`: a folder containing filtered gnomAD variants organized by gene symbol (in vcf format)  
├── `gene_list.txt`: [optional] via helper script to generate gene list according to SFARI filtering criteria  
└── `main.csv` the output file  

#### CSV Feature Columns
- `Gene Symbol`: string (e.g. MYH9, ACTB)  
- `HGNC`: integer ID (e.g. 7579, 132) (via DIOPT)  
- `Source`: db_name | db_name | ...  
- `SFARI Score`: 1,2,S,1S,2S,3S   
###### DIOPT  
- `Best DIOPT Score (Fly)`: integer score
- `Symbol (Fly)`: string (e.g. zip, Act5C)
- `Best Ortholog (Fly)`: boolean
- `Best DIOPT Score (Yeast)`: integer score
- `Symbol (Yeast)`: string (e.g. MYO1, ACT1)
- `Best Ortholog (Yeast)`: boolean
###### ClinVar  
- `ClinVar: Pathogenic & Likely Pathogenic`: count
- `ClinVar: Benign & Likely Benign`: count
- `ClinVar: VUS`: count
- `ClinVar: Conflicting`: count

### Project Code DIR
├── `/utils` helper scripts  
├── `main.py` main pipeline  
├── `main.sh`  bash script to wrap main pipeline for easier queues/runs  
└── `README.md`
