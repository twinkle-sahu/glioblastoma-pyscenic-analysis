# Single-Cell Regulatory Network Analysis in Glioblastoma (GSE214966)

## 1. Research Question
What are the core transcription factor master regulators and distinct cell-state activity patterns driving cellular heterogeneity and transcriptional states in glioblastoma tumor samples?

## 2. Data Source
* **Dataset:** GSE214966 (Single-cell RNA sequencing of human glioblastoma brain cells)
* **Repository:** NCBI Gene Expression Omnibus (GEO)
* **Processed Dimensions:** 6,374 cells × 15,668 genes (`gbm_brain_cells.loom`)

## 3. Method & Pipeline Overview
* **Co-expression Module Inference (`pyscenic_motif.py`):** Uses GRNBoost2 to infer candidate transcriptional regulatory relationships from the single-cell expression matrix based on gene co-expression patterns.
* **Cis-Regulatory Motif Enrichment (`pyscenic_motif.py`):** Uses RcisTarget to analyze promoter motif enrichment around target gene transcription start sites (TSS), filtering co-expression modules into high-confidence regulons.
* **Cellular Activity Scoring (`pyscenic_aucell.py`):** Uses AUCell to calculate the activity of each regulon in individual cells, generating a cell-by-regulon activity score matrix.
* **Visualization (`pyscenic_visualization.py`):** Generates publication-ready hierarchical clustering heatmaps displaying regulon activity scores across glioblastoma cellular states.
* **Topological Null Model Validation (`null_model_comparison.py`):** Compares the inferred network against an Erdős-Rényi random graph null baseline ($G(n, p)$ model with matching node count $n=400$) to evaluate network density and structural organization.

## 4. How to Run the Code
1. Clone or download this repository onto your local machine.
2. Install the required Python environment dependencies:
   ```bash
   pip install -r requirements.txt
