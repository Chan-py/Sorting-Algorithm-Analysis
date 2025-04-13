import matplotlib.pyplot as plt
import numpy as np

# 분포 라벨
# distributions = ['random', 'sorted', 'reverse', 'partially', 'same_element']
# x = np.arange(len(distributions))

# # CLRS와 DS 시간 (단위: 초)
# # random : 0.015, 0.014
# # sorted : 4.684, 1.612
# # reverse : 2.234, 1.176
# # partially : 0.561, 0.015
# # same_element : 4.627, 0.010
# times_clrs = [0.015, 4.684, 2.234, 0.561, 4.627]
# times_ds   = [0.014, 1.612, 1.176, 0.015, 0.010]

# bar_width = 0.3

# plt.figure(figsize=(8, 5))

# # 첫 번째 막대: CLRS
# plt.bar(x - bar_width/2, times_clrs, width=bar_width, label='CLRS', color='skyblue')
# # 두 번째 막대: DS
# plt.bar(x + bar_width/2, times_ds,   width=bar_width, label='DS',   color='tomato')

# plt.xticks(x, distributions, rotation=15)   # x축에 배치된 5개 라벨 표시
# plt.xlabel("Data Distribution")
# plt.ylabel("Time (seconds)")
# plt.title("Comparison: CLRS vs. DS (Quick Sort, 10K)")

# plt.legend()
# plt.tight_layout()

# # 그래프를 파일로 저장
# plt.savefig("exp3_clrs_ds_comparison.png", dpi=300, bbox_inches='tight')
# plt.show()


# # 세 가지 데이터셋 라벨
# distributions = ['sorted', 'reverse', 'partially']
# x = np.arange(len(distributions))  # [0,1,2]

# # (기존) 퀵소트와 랜덤 퀵소트 실행 시간 (정렬된 순서: sorted, reverse, partially)
# times_quick = [4.718, 2.330, 0.541]
# times_rand  = [0.017, 0.018, 0.021]

# bar_width = 0.3

# plt.figure(figsize=(8, 5))

# # 첫 번째 막대: 일반 Quick Sort
# plt.bar(x - bar_width/2, times_quick, width=bar_width, label='Quick Sort', color='skyblue')
# # 두 번째 막대: Randomized Quick Sort
# plt.bar(x + bar_width/2, times_rand,  width=bar_width, label='Randomized Quick', color='tomato')

# plt.xticks(x, distributions)
# plt.xlabel("Data Distribution")
# plt.ylabel("Time (seconds)")
# plt.title("Comparison: Quick vs. Randomized Quick (10K)")

# plt.legend()
# plt.tight_layout()

# # 그래프 파일로 저장
# plt.savefig("exp3_quick_vs_randomized_comparison.png", dpi=300, bbox_inches='tight')
# plt.show()


# (기존) Quick Sort와 Dual-Pivot Quick Sort의 실행 시간
# 10K : 0.018, 0.017
# 100K : 0.275, 0.208
# 1M : 9.901, 5.076

times_quick       = [0.018, 0.275, 9.901]
times_dual_pivot  = [0.017, 0.208, 5.076]

size_labels = ["10K", "100K", "1M"]

fig, axes = plt.subplots(1, 3, figsize=(12, 4))  # 가로로 3개 subplot

for i in range(3):
    # i번째 subplot에 대한 2개의 값(Quick, DualPivot)
    y = [times_quick[i], times_dual_pivot[i]]
    x = np.arange(len(y))  # [0, 1]

    axes[i].bar(x, y, width=0.6, color=['skyblue', 'tomato'])
    
    # x축 라벨 2개: 'Quick' vs 'DualPivot'
    axes[i].set_xticks(x)
    axes[i].set_xticklabels(["Quick", "DualPivot"], rotation=15)

    # subplot 제목으로 배열 크기 표기
    axes[i].set_title(size_labels[i])

    # 첫 번째 subplot에만 y축 라벨 표시
    if i == 0:
        axes[i].set_ylabel("Time (sec)")

plt.suptitle("Comparison: Quick vs. Dual-Pivot Quick", fontsize=14)
plt.tight_layout()

# 그래프 저장
plt.savefig("exp3_quick_vs_dual_pivot.png", dpi=300, bbox_inches='tight')
plt.show()