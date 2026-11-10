import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

if __name__ == '__main__':
    output_dir = r'C:\Users\twinkle\Downloads\System_Bio_Project\DATA'
    auc_output_path = os.path.join(output_dir, 'aucell_activity_matrix.csv')
    heatmap_output_path = os.path.join(output_dir, 'glioblastoma_regulon_heatmap.png')

    print("Loading AUCell activity score matrix...")
    auc_matrix = pd.read_csv(auc_output_path, index_col=0)

    print("Generating regulon activity heatmap...")
    plt.figure(figsize=(10, 8))
    sns.clustermap(
        auc_matrix.sample(n=min(500, len(auc_matrix)), random_state=42),
        cmap="viridis",
        standard_scale=1,
        figsize=(10, 8),
        col_cluster=True,
        row_cluster=True
    )
    plt.savefig(heatmap_output_path, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Heatmap saved to: {heatmap_output_path}")