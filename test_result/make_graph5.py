import json
import matplotlib.pyplot as plt
import numpy as np

# Load results.json
with open('results.json', 'r') as f:
    data = json.load(f)

# --------------------------------------------------------------------
# (1) Quick Sort vs Intro Sort on Random Data across sizes 1K, 10K, 100K, 1M
# --------------------------------------------------------------------
sizes = ['1K', '10K', '100K', '1M']
keys = [f'{s}_random' for s in sizes]
quick_times = [data[k]['quick_sort'] for k in keys]
intro_times = [data[k]['intro_sort'] for k in keys]

fig, axes = plt.subplots(1, 4, figsize=(16, 4))
for i, size in enumerate(sizes):
    axes[i].bar(['Quick Sort', 'Intro Sort'], [quick_times[i], intro_times[i]],
                color=['skyblue', 'tomato'], width=0.6)
    axes[i].set_title(f'{size} random')
    if i == 0:
        axes[i].set_ylabel('Time (seconds)')
    axes[i].set_ylim(0, max(quick_times[i], intro_times[i]) * 1.2)

plt.suptitle('Quick Sort vs Intro Sort on Random Data (1K to 1M)', fontsize=14)
plt.tight_layout()
plt.savefig('figures/exp6_quick_vs_intro_random_sizes.png', dpi=300, bbox_inches='tight')
plt.show()

# --------------------------------------------------------------------
# (2) Quick Sort vs Intro Sort on 100K for various distributions
# --------------------------------------------------------------------
distributions = ['sorted', 'reverse_sorted', 'partially_sorted']

# Times for first three distributions
quick_times = [data[f'100K_{d}']['quick_sort'] for d in distributions[:-1]]
intro_times = [data[f'100K_{d}']['intro_sort'] for d in distributions[:-1]]

# Compute average for partially_sorted_1,2,3
partial_keys = [f'100K_partially_sorted_{i}' for i in (1, 2, 3)]
quick_partial_avg = np.mean([data[k]['quick_sort'] for k in partial_keys])
intro_partial_avg = np.mean([data[k]['intro_sort'] for k in partial_keys])

quick_times.append(quick_partial_avg)
intro_times.append(intro_partial_avg)

# Plot grouped bar chart
x = np.arange(len(distributions))
bar_width = 0.35

plt.figure(figsize=(8, 5))
plt.bar(x - bar_width/2, quick_times, bar_width, label='Quick Sort', color='skyblue')
plt.bar(x + bar_width/2, intro_times, bar_width, label='Intro Sort', color='tomato')

plt.xticks(x, distributions, rotation=15)
plt.xlabel('Data Distribution (100K)')
plt.ylabel('Time (seconds)')
plt.title('Quick Sort vs Intro Sort on 100K by Distribution')
plt.legend()
plt.ylim(0, max(max(quick_times), max(intro_times)) * 1.2)

plt.tight_layout()
plt.savefig('figures/exp6_quick_vs_intro_100K_distros.png', dpi=300, bbox_inches='tight')
plt.show()