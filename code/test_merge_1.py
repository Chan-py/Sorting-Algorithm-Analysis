import time
from conventional_algorithms import merge_sort, heap_sort, bubble_sort, insertion_sort, selection_sort, quick_sort
from utils import check_sorted, read_list_from_txt
import matplotlib.pyplot as plt

dataset = []
arr = read_list_from_txt("../dataset/real/100K_partially_sorted_3.txt")

result_a = []
result_b = []
for i in range(100):
    print("Current iteration: ", i+1)
    arr_a = arr[:]
    n = len(arr_a)
    start_time = time.time()
    merge_sort.merge_sort(arr_a, 0, n-1)
    end_time = time.time()
    result_a.append(end_time - start_time)

    arr_b = arr[:]
    n = len(arr_b)
    start_time = time.time()
    merge_sort.merge_sort_without_sentinel(arr_b, 0, n-1)
    end_time = time.time()
    result_b.append(end_time - start_time)


# 1) 평균 시간 계산
avg_a = sum(result_a) / len(result_a)
avg_b = sum(result_b) / len(result_b)

print(avg_a)
print(avg_b)

# # 2) 그래프 데이터를 준비
# labels = ['With Sentinel', 'Without Sentinel']
# values = [avg_a, avg_b]

# # 3) 막대 그래프 생성
# x = [0, 1]
# plt.bar(x, values, width=0.4)
# plt.xticks(x, labels)
# plt.xlim(-0.5, 1.5)

# # 4) y축 최댓값을 조금 여유 있게 설정
# ymax = max(values) * 1.4
# plt.ylim(0, ymax)

# # 5) 그래프 꾸미기
# plt.title("Comparison of Merge Sort (Sentinel vs. No Sentinel)")
# plt.xlabel("Method")
# plt.ylabel("Average Time (seconds)")

# # 6) 화면에 표시
# plt.savefig("../test_result/merge_sort_sentinel.png", dpi=300, bbox_inches='tight')
# plt.show()