import json
import pandas as pd
import numpy as np

# 1) Load results.json
with open('results.json', 'r') as f:
    data = json.load(f)

# 2) Define distributions and sizes
distributions = [
    'random', 'sorted', 'reverse_sorted',
    'partially_sorted_1', 'partially_sorted_2', 'partially_sorted_3',
    'same_element'
]
sizes = ['1K', '10K', '100K', '1M']

# 3) Build the ordered list of dataset keys
dataset_keys = []
for dist in distributions:
    for size in sizes:
        dataset_keys.append(f'{size}_{dist}')

# 4) Create DataFrame: rows=dataset keys, cols=algorithms
#    pd.DataFrame(data).T → rows are dataset keys, columns are algorithm names
df = pd.DataFrame(data).T

# 5) Reindex the rows (index) to include all dataset_keys (missing → NaN)
df = df.reindex(dataset_keys)

# 6) Fill missing entries with infinity
df = df.fillna(np.inf)

# 7) Now df.index is dataset_keys, df.columns is algorithms
#    If you want algorithms as rows and datasets as columns, transpose:
df_algorithms = df.T

# 8) Inspect or save
print(df_algorithms)                   # 콘솔에 출력
df_algorithms.to_csv('overview.csv')   # CSV로 저장