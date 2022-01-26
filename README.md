# [SFARI] ASD Gene Selection
ASD gene selection/prioritization pipeline for SFARI project. Ref Aim 1.1 in Project Proposal Narative.

### Directories (DIR)
Overviews of important project DIRs listed in this section.
 
#### Input (Data) DIR
(*Date of file versions to be updated)
/cosmos/data/project-data/SFARI-ASD_Gene_Selection-data/  
├── `gene_list.txt (SFARI gene list)`  
├── `SFARI-Gene_genes_09-02-2021release_01-12-2022export.csv`  
├── `DIOPTvs8.zip`  
├── `clinvar_2021.vcf.gz`  

#### Output (Results) DIR
/home/kchen/results/SFARI-ASD_Gene_Selection-out/  
├── `dict_<db>.pickle` where <db> is replaced by various database names  
└── `main.csv` the output file  

###### CSV Feature Columns
- `Gene Symbol`
- `Source`
- `SFARI Score`
- `ClinVar: Pathogenic & Likely Pathogenic`
- `ClinVar: Benign & Likely Benign`
- `ClinVar: VUS`
- `ClinVar: Conflicting`

#### Project Code DIR
├── `/utils` helper scripts  
├── `main.py` main pipeline  
├── `main.sh`  bash script to wrap main pipeline for easier queues/runs
└── `README.md`
