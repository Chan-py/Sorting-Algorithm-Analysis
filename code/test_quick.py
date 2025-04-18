import time
from conventional_algorithms import merge_sort, heap_sort, bubble_sort, insertion_sort, selection_sort, quick_sort
from utils import check_sorted, read_list_from_txt

import sys
sys.setrecursionlimit(10**6)

dataset = []
arr = read_list_from_txt("../dataset/real/1K_random.txt")

result_a = []
result_b = []
for i in range(10):
    print("Current iteration : ", i+1)
    arr_a = arr[:]
    n = len(arr_a)
    start_time = time.time()
    quick_sort.quick_sort(arr_a, 0, n-1)
    end_time = time.time()
    result_a.append(end_time - start_time)

    arr_b = arr[:]
    n = len(arr_b)
    start_time = time.time()
    quick_sort.dual_pivot_quick_sort(arr_b, 0, n-1)
    end_time = time.time()
    result_b.append(end_time - start_time)

print(sum(result_a) / len(result_a))
print(sum(result_b) / len(result_b))