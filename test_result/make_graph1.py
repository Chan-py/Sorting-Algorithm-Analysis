import matplotlib.pyplot as plt
import numpy as np

# --------------------------------------------------------------------
# (1) 사이즈별 비교 결과: 서브플롯 3개
# --------------------------------------------------------------------

# 예시 데이터 (Insertion, Library, Binary Insertion)
times_insertion   = [0.011, 1.23, 177.846]    # 1K, 10K, 100K
times_library     = [0.013, 1.18, 234.408]
times_bin_inser   = [0.007, 0.80, 92.462]

size_labels = ['1K', '10K', '100K']
algo_labels = ['Insertion', 'Library', 'Binary Insertion']
colors = ['skyblue', 'tomato', 'lightgreen']

fig, axes = plt.subplots(1, 3, figsize=(12, 4))  # 한 줄에 3개 subplot

for i in range(3):
    y = [
        times_insertion[i],
        times_library[i],
        times_bin_inser[i]
    ]
    x = np.arange(len(y))  # [0,1,2]
    
    axes[i].bar(x, y, width=0.6, color=colors)
    
    axes[i].set_xticks(x)
    axes[i].set_xticklabels(algo_labels, rotation=15)
    axes[i].set_title(size_labels[i])
    
    if i == 0:
        axes[i].set_ylabel("Time (sec)")

plt.suptitle("Experiment 2 (Size-based): Comparison Among 3 Sorts", fontsize=14)
plt.tight_layout()

# 그래프 저장
plt.savefig("exp2_size_comparison.png", dpi=300, bbox_inches='tight')
plt.show()


# --------------------------------------------------------------------
# (2) 다양성별 비교 (10K 데이터) : grouped bar chart
# --------------------------------------------------------------------
distributions = ['random', 'sorted', 'reverse', 'partial']
x2 = np.arange(len(distributions)) 

insertion_times  = [1.23, 0.0006, 2.36, 1.03]
library_times    = [1.18, 0.016, 4.90, 1.10]
bin_inser_times  = [0.80, 0.008, 1.66, 0.66]

bar_width = 0.25

plt.figure(figsize=(8, 5))

plt.bar(x2 - bar_width, insertion_times, bar_width, label='Insertion Sort', color='skyblue')
plt.bar(x2,            library_times,   bar_width, label='Library Sort',    color='tomato')
plt.bar(x2 + bar_width, bin_inser_times, bar_width, label='Binary Insertion', color='lightgreen')

plt.xticks(x2, distributions)
plt.xlabel("Data Distribution")
plt.ylabel("Time (seconds)")
plt.title("Experiment 2 (Diversity-based): 10K Data, 3 Sorts")
plt.legend()

plt.tight_layout()

# 그래프 저장
plt.savefig("exp2_diversity_comparison.png", dpi=300, bbox_inches='tight')
plt.show()
