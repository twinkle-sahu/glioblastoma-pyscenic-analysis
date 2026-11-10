import numpy as np
if not hasattr(np, 'object'):
    np.object = object

import os
import loompy as lp
import pandas as pd

if __name__ == '__main__':
    output_dir = r'C:\Users\twinkle\Downloads\System_Bio_Project\DATA'
    loom_path = r'C:\Users\twinkle\Downloads\System_Bio_Project\DATA\gbm_brain_cells.loom'
    regulons_path = os.path.join(output_dir, 'regulons.csv')
    auc_output_path = os.path.join(output_dir, 'aucell_activity_matrix.csv')

    print("Loading regulons definition...")
    regulons_df = pd.read_csv(regulons_path)

    print("Reading expression matrix from .loom file...")
    with lp.connect(loom_path, mode='r') as ds:
        expr_mat = pd.DataFrame(ds[:, :], index=ds.row_attrs["Gene"], columns=ds.col_attrs["CellID"])

    ex_matrix = expr_mat.T

    print("Calculating regulon activity scores...")
    activity_scores = {}
    for tf, group in regulons_df.groupby('TF'):
        targets = [t for t in group['target'].unique() if t in ex_matrix.columns]
        if len(targets) > 0:
            activity_scores[tf] = ex_matrix[targets].mean(axis=1)

    auc_matrix = pd.DataFrame(activity_scores)
    auc_matrix.to_csv(auc_output_path)
    print(f"Saved to: {auc_output_path}")