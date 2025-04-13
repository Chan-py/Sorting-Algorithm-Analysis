import json
import matplotlib.pyplot as plt
import numpy as np

# Load results.json
with open('results.json', 'r') as f:
    data = json.load(f)

# --------------------------------------------------------------------
# (1) Bubble vs Cocktail Shaker vs Comb on Random Data across sizes 1K, 10K, 100K
# --------------------------------------------------------------------
sizes = ['1K', '10K', '100K']
keys = [f'{s}_random' for s in sizes]
bubble_times   = [data[k]['bubble_sort'] for k in keys]
cocktail_times = [data[k]['cocktail_shaker_sort'] for k in keys]
comb_times     = [data[k]['comb_sort'] for k in keys]

fig, axes = plt.subplots(1, 3, figsize=(15, 4))
colors = ['skyblue', 'tomato', 'lightgreen']

for i, size in enumerate(sizes):
    y = [bubble_times[i], cocktail_times[i], comb_times[i]]
    axes[i].bar(['Bubble', 'Cocktail', 'Comb'], y, color=colors, width=0.6)
    axes[i].set_title(f'{size} Random')
    if i == 0:
        axes[i].set_ylabel('Time (seconds)')
    axes[i].set_ylim(0, max(y) * 1.2)

plt.suptitle('Bubble vs Cocktail Shaker vs Comb Sort on Random Data (1K to 100K)', fontsize=14)
plt.tight_layout()
plt.savefig('figures/exp5_bubble_cocktail_comb_random_sizes.png', dpi=300, bbox_inches='tight')
plt.show()

# --------------------------------------------------------------------
# (2) Bubble vs Cocktail Shaker vs Comb on 100K for various distributions
# --------------------------------------------------------------------
distributions = ['random', 'sorted', 'reverse_sorted', 'partially_sorted']

# Gather times for first three distributions
bubble_times   = [data[f'100K_{d}']['bubble_sort'] for d in distributions[:-1]]
cocktail_times = [data[f'100K_{d}']['cocktail_shaker_sort'] for d in distributions[:-1]]
comb_times     = [data[f'100K_{d}']['comb_sort'] for d in distributions[:-1]]

# Compute average for partially_sorted_1,2,3
parts = [f'100K_partially_sorted_{i}' for i in (1, 2, 3)]
bubble_avg   = np.mean([data[k]['bubble_sort'] for k in parts])
cocktail_avg = np.mean([data[k]['cocktail_shaker_sort'] for k in parts])
comb_avg     = np.mean([data[k]['comb_sort'] for k in parts])

bubble_times.append(bubble_avg)
cocktail_times.append(cocktail_avg)
comb_times.append(comb_avg)

# Plot grouped bar chart
x = np.arange(len(distributions))
bar_width = 0.25

plt.figure(figsize=(8, 5))
plt.bar(x - bar_width, bubble_times,   bar_width, label='Bubble Sort',         color='skyblue')
plt.bar(x,            cocktail_times, bar_width, label='Cocktail Shaker Sort', color='tomato')
plt.bar(x + bar_width, comb_times,    bar_width, label='Comb Sort',            color='lightgreen')

plt.xticks(x, distributions, rotation=15)
plt.xlabel('Data Distribution (100K)')
plt.ylabel('Time (seconds)')
plt.title('Bubble vs Cocktail Shaker vs Comb Sort on 100K by Distribution')
plt.legend()
plt.ylim(0, max(max(bubble_times), max(cocktail_times), max(comb_times)) * 1.2)

plt.tight_layout()
plt.savefig('figures/exp5_bubble_cocktail_comb_100K_distros.png', dpi=300, bbox_inches='tight')
plt.show()