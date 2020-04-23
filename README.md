# SARS_Cov2_Classifier
The main objective of this project is to classify the different nucleotide genomes coming from various sources and build a classifier to serve that purpose.

**Data Source:** https://www.ncbi.nlm.nih.gov/labs/virus/vssi

**sequences.fasta** and **sequences.csv** contain data collected from the above link (updated as of 12 pm 23/4/2020).
**final.csv** contains combined data from the above files.

Use *pip install -r requirements.txt* inside the virtual env to download the necessary packages.

### File Descriptions:
**create_dataset.ipynb:** Combines data from sequences.fasta and sequences.csv to generate the dataset in final.csv.
**encoder.ipynb:** Encodes neucleotide sequences following ordinal encoding scheme (Paper:https://www.biorxiv.org/content/10.1101/186965v2.full.pdf) 
