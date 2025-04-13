import time
from conventional_algorithms import merge_sort, heap_sort, bubble_sort, insertion_sort, selection_sort, quick_sort
from contemporary_algorithms import library_sort, tim_sort, cocktail_shaker_sort, comb_sort, tournament_sort, intro_sort
from utils import check_sorted, read_list_from_txt

import sys
sys.setrecursionlimit(10**6)

dataset = [
    "1M_same_element"
]
for ds in dataset:
    arr = read_list_from_txt(f"../dataset/real/{ds}.txt")

    result_a = []
    result_b = []
    for i in range(10):
        print("Current iteration : ", i+1)
        arr_a = arr[:]
        n = len(arr_a)
        start_time = time.time()
        library_sort.run(arr_a)
        end_time = time.time()
        result_a.append(end_time - start_time)

    print(ds)
    print(sum(result_a) / len(result_a))