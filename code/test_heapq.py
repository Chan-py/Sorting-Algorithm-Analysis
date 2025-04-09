import time
from conventional_algorithms import merge_sort, heap_sort, bubble_sort, insertion_sort, selection_sort, quick_sort
from utils import check_sorted, read_list_from_txt

dataset = []
arr = read_list_from_txt("../dataset/real/10K_random.txt")

result_a = []
result_b = []
for i in range(10):
    arr_a = arr[:]
    n = len(arr_a)
    start_time = time.time()
    heap_sort.Heap_sort(arr_a)
    end_time = time.time()
    result_a.append(end_time - start_time)

    arr_b = arr[:]
    n = len(arr_b)
    start_time = time.time()
    heap_sort.heap_sort_lib(arr_b)
    end_time = time.time()
    result_b.append(end_time - start_time)
    check_sorted(arr_b)

print(sum(result_a) / 10)
print(sum(result_b) / 10)