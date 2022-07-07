# [SFARI] ASD Gene Selection
ASD gene selection/prioritization pipeline for SFARI project. Ref Aim 1.1 in Project Proposal Narative. 
Reference genome hg19 for all databases used.

## Directories (DIR)
Overviews of important project DIRs listed in this section.

### Project Code DIR
├── `/data_ingestion` database ingestion scripts (processing raw bulk data files into a workable format)  
├── `/feature_extraction` feature extraction scripts (extracting/retaining features we want-- can include project-specific filter criteria)  
├── `/utils` helper scripts  
│   ├── `get_main_csv.py` get csv from dict_main.pickle (in pipeline)  
│   └── `get_input.sh` script to wget most of the input files  
├── `main.sh` main pipeline    
├── `run_main.sh` sample bash script of how main pipeline can be run  
├── `requirements.txt`  
└── `README.md`  
 
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

## CSV Feature Columns
- `Gene Symbol`: string (e.g. MYH9, ACTB)  
- `HGNC`: integer ID (e.g. 7579, 132) (via DIOPT)  
- `Source`: db_name | db_name | ...  
- `SFARI Score`: 1,2,S,1S,2S,3S   
- `Gene Name`
- `Previous Gene Symbol(s)`
- `NCBI Entrez ID`
- `UniProt ID`
- `HGNC`
###### DIOPT  
- `Depth of Conservation`: Number of species gene is conserved in (out of 8)
- `Best DIOPT Score (Fly)`: integer score  
- `Symbol (Fly)`: string (e.g. zip, Act5C)  
- `Flybase ID`: string (e.g. FBgn0265434)  
- `Best Ortholog (Fly)`: boolean  
- `Fly Alignment Similarity (%)` and `Fly Alignment Identity (%)`  
- `Best DIOPT Score (Yeast)`: integer score  
- `Symbol (Yeast)`: string (e.g. MYO1, ACT1)
- `SGD ID`: string (e.g. S000001065)
- `Best Ortholog (Yeast)`: boolean
- `Yeast Alignment Similarity (%)` and `Yeast Alignment Identity (%)`  
###### ClinVar  
- `ClinVar: Pathogenic & Likely Pathogenic`: count
- `ClinVar: Benign & Likely Benign`: count
- `ClinVar: VUS`: count
- `ClinVar: Conflicting`: count  
- `ClinVar Phenotype`
###### Gene2PubMed
- `Number of Publications`
###### VariCarta
- `Number of De Novo (VariCarta)`
- `Number of Missense (VariCarta)`
###### gnomAD
- `Chromosome`, `Starting Position`, `End Position`
- `mis_z`,	`oe_mis`,	`oe_mis_lower`,	`oe_mis_upper`,	`pLI	oe_lof`,	`oe_lof_lower`,	`oe_lof_upper`: see https://genome.ucsc.edu/cgi-bin/hgTrackUi?db=hg19&g=gnomadPLI for documentation on stats
- `gnomAD Variant Count`: variant counts per gene with MAF > 1e-4. Qualifying variants are stored.
###### Flybase
- `Flybase Snapshot`	
- `Flybase datestamp`: most recent update in Flybase
- `Flybase: Gene Summary`
###### Gene Ontology
- link to GO web page for each gene
 
 
 ### Notes
 - PubMed counts will yield -1 for outdated gene symbols. Please replace with the most recent symbol.  


