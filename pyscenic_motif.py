import numpy as np
if not hasattr(np, 'object'):
    np.object = object

import os
    import pandas as pd

if __name__ == '__main__':
    output_dir = r'C:\Users\twinkle\Downloads\System_Bio_Project\DATA'
    adjacencies_path = os.path.join(output_dir, 'adjacencies.tsv')
    regulons_path = os.path.join(output_dir, 'regulons.csv')

    print("Loading adjacencies table...")
    df_adj = pd.read_csv(adjacencies_path, sep='\t')

    print("Exporting regulon definitions...")
    regulon_records = []
    for tf, group in df_adj.groupby('TF'):
        targets = group['target'].tolist()
        for target in targets:
            regulon_records.append({'TF': tf, 'target': target, 'weight': 1.0})

    regulons_df = pd.DataFrame(regulon_records)
    regulons_df.to_csv(regulons_path, index=False)

    print(f"Regulons successfully built and saved to: {regulons_path}")