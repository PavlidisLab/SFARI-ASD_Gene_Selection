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
- `HGNC`: integer ID (e.g. 7579, 132) (via DIOPT)
- `Source`: db_name | db_name | ...
- `SFARI Score`: 1,2,S,1S,2S,3S  
###### DIOPT  
- `Best DIOPT Score (Fly)`: integer score
- `Symbol (Fly)`: string (e.g. zip, Act5C)
- `Best Ortholog (Fly)`: boolean (Y,N)
- `Best DIOPT Score (Yeast)`: integer score
- `Symbol (Yeast)`: string (e.g. MYO1, ACT1)
- `Best Ortholog (Yeast)`: boolean (Y,N)
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
