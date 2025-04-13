import time
from conventional_algorithms import merge_sort, heap_sort, bubble_sort, insertion_sort, selection_sort, quick_sort
from contemporary_algorithms import library_sort, tim_sort, cocktail_shaker_sort, comb_sort, tournament_sort, intro_sort
from utils import check_sorted, read_list_from_txt

dataset = []
arr = read_list_from_txt("../dataset/real/10K_random.txt")

result_a = []
result_b = []
result_c = []
for i in range(5):
    print("Current iteration : ", i+1)
    arr_a = arr[:]
    n = len(arr_a)
    start_time = time.time()
    insertion_sort.insertion_sort(arr_a)
    end_time = time.time()
    result_a.append(end_time - start_time)

    arr_b = arr[:]
    n = len(arr_b)
    start_time = time.time()
    library_sort.library_sort(arr_b)
    end_time = time.time()
    result_b.append(end_time - start_time)

    arr_c = arr[:]
    n = len(arr_c)
    start_time = time.time()
    insertion_sort.insertion_sort_binary(arr_c)
    end_time = time.time()
    result_c.append(end_time - start_time)

print(sum(result_a) / len(result_a))
print(sum(result_b) / len(result_b))
print(sum(result_c) / len(result_c))