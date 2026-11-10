"""
Data Download Instructions for GSE214966 Glioblastoma Dataset
-----------------------------------------------------------
The raw single-cell RNA-seq count matrix and metadata for GSE214966 
can be downloaded directly from the NCBI Gene Expression Omnibus (GEO):
URL: https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE214966

Note: Large raw data files (like 'gbm_brain_cells.loom') are excluded 
from version control per repository guidelines. Place the downloaded 
'.loom' file into the local DATA/ directory before running the pipeline.
"""

import os

if __name__ == "__main__":
    print("Please download dataset GSE214966 from NCBI GEO.")
    print("Expected local path: C:\\Users\\twinkle\\Downloads\\System_Bio_Project\\DATA\\gbm_brain_cells.loom")