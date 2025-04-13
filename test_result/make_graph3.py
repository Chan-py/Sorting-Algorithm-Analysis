import json
import matplotlib.pyplot as plt
import numpy as np

# Load results.json
with open('results.json', 'r') as f:
    data = json.load(f)

# --------------------------------------------------------------------
# (1) Merge Sort vs Timsort on Random Data across sizes 1K, 10K, 100K, 1M
# --------------------------------------------------------------------
sizes = ['1K', '10K', '100K', '1M']
keys = [f'{s}_random' for s in sizes]
merge_times = [data[k]['merge_sort'] for k in keys]
tim_times   = [data[k]['tim_sort']  for k in keys]

fig, axes = plt.subplots(1, 4, figsize=(16, 4))
for i, size in enumerate(sizes):
    axes[i].bar(['Merge Sort', 'Timsort'], [merge_times[i], tim_times[i]],
                color=['skyblue', 'tomato'], width=0.6)
    axes[i].set_title(f'{size} random')
    if i == 0:
        axes[i].set_ylabel('Time (seconds)')
    axes[i].set_ylim(0, max(merge_times[i], tim_times[i]) * 1.2)

plt.suptitle('Merge Sort vs Timsort on Random Data (1K to 1M)', fontsize=14)
plt.tight_layout()
plt.savefig('figures/exp4_merge_vs_tim_random_sizes.png', dpi=300, bbox_inches='tight')
plt.show()

# --------------------------------------------------------------------
# (2) Merge Sort vs Timsort on 100K for various distributions
# --------------------------------------------------------------------
distributions = ['random', 'sorted', 'reverse_sorted', 'partially_sorted']
# Gather times for first three
merge_times = [data[f'100K_{d}']['merge_sort'] for d in distributions[:-1]]
tim_times   = [data[f'100K_{d}']['tim_sort']   for d in distributions[:-1]]

# Average for partially_sorted_1,2,3
parts = [f'100K_partially_sorted_{i}' for i in (1, 2, 3)]
merge_avg = np.mean([data[k]['merge_sort'] for k in parts])
tim_avg   = np.mean([data[k]['tim_sort']   for k in parts])
merge_times.append(merge_avg)
tim_times.append(tim_avg)

x = np.arange(len(distributions))
bar_width = 0.35

fig, ax = plt.subplots(figsize=(8, 5))
ax.bar(x - bar_width/2, merge_times, bar_width, label='Merge Sort', color='skyblue')
ax.bar(x + bar_width/2, tim_times,   bar_width, label='Timsort',    color='tomato')

ax.set_xticks(x)
ax.set_xticklabels(distributions, rotation=15)
ax.set_xlabel('Data Distribution (100K)')
ax.set_ylabel('Time (seconds)')
ax.set_title('Merge Sort vs Timsort on 100K by Distribution')
ax.legend()
ax.set_ylim(0, max(max(merge_times), max(tim_times)) * 1.2)

plt.tight_layout()
plt.savefig('figures/exp4_merge_vs_tim_100K_distros.png', dpi=300, bbox_inches='tight')
plt.show()