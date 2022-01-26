# [SFARI] ASD Gene Selection
ASD gene selection/prioritization pipeline for SFARI project. Ref Aim 1.1 in Project Proposal Narative.

## Directories (DIR)
Overviews of important project DIRs listed in this section.
 
### Input (Data) DIR
(*Date of file versions to be updated)
/cosmos/data/project-data/SFARI-ASD_Gene_Selection-data/  
├── `gene_list.txt (SFARI gene list)`  
├── `SFARI-Gene_genes_09-02-2021release_01-12-2022export.csv`  
├── `DIOPTvs8.zip`  
├── `clinvar_2021.vcf.gz`  

### Output (Results) DIR
/home/kchen/results/SFARI-ASD_Gene_Selection-out/  
├── `dict_<db>.pickle` where <db> is replaced by various database names  
└── `main.csv` the output file  

#### CSV Feature Columns
- `Gene Symbol`: string (e.g. MYH9, ACTB)
- `Source`: db_name | db_name | db_name
- `SFARI Score`: 1,2,S,1S,2S,3S  
###### DIOPT  
- `Fly Symbol`: string (e.g. zip, Act5C)
- `Best Fly Ortholog`: boolean (Y,N)
- `Yeast Symbol`: string (e.g. MYO1, ACT1)
- `Best Yeast Ortholog`: boolean (Y,N)
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
