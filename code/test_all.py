import time
import json
import sys
sys.setrecursionlimit(10**6)

from conventional_algorithms import merge_sort, heap_sort, bubble_sort, insertion_sort, selection_sort, quick_sort
from contemporary_algorithms import library_sort, tim_sort, cocktail_shaker_sort, comb_sort, tournament_sort, intro_sort

from utils import check_sorted, read_list_from_txt

# 1) 데이터셋 목록을 문자열로 저장
dataset = [
    "1K_random", "1K_sorted", "1K_reverse_sorted", "1K_partially_sorted_1", "1K_partially_sorted_2", "1K_partially_sorted_3", "1K_same_element",
    "10K_random", "10K_sorted", "10K_reverse_sorted", "10K_partially_sorted_1", "10K_partially_sorted_2", "10K_partially_sorted_3", "10K_same_element",
    "100K_random", "100K_sorted", "100K_reverse_sorted", "100K_partially_sorted_1", "100K_partially_sorted_2", "100K_partially_sorted_3", "100K_same_element",
    "1M_random", "1M_sorted", "1M_reverse_sorted", "1M_partially_sorted_1", "1M_partially_sorted_2", "1M_partially_sorted_3", "1M_same_element"
]

# 2) 12개 알고리즘을 (이름 → 실행 함수) 형태로 등록
#    예시로, bubble_sort.run(arr)를 호출하려면 람다로 감싸서 사용
algo_dict = {
    "merge_sort": lambda arr: merge_sort.run(arr),
    "heap_sort": lambda arr: heap_sort.run(arr),
    "bubble_sort": lambda arr: bubble_sort.run(arr),
    "insertion_sort": lambda arr: insertion_sort.run(arr),
    "selection_sort": lambda arr: selection_sort.run(arr),
    "quick_sort": lambda arr: quick_sort.run(arr),

    "library_sort": lambda arr: library_sort.run(arr),
    "tim_sort": lambda arr: tim_sort.run(arr),
    "cocktail_shaker_sort": lambda arr: cocktail_shaker_sort.run(arr),
    "comb_sort": lambda arr: comb_sort.run(arr),
    "tournament_sort": lambda arr: tournament_sort.run(arr),
    "intro_sort": lambda arr: intro_sort.run(arr),
}

# O(n^2) 알고리즘 (대규모 데이터셋에서 제외)
n2_algos = {"bubble_sort", "insertion_sort", "selection_sort",
            "cocktail_shaker_sort", "comb_sort", "quick_sort", "library_sort"}

# 3) 결과 저장용 딕셔너리: { dataset_name: { algo_name: avg_time, ... }, ... }
all_results = {}

# 4) 각 데이터셋에 대해 실행
for ds in dataset[17:]:
    print("Current dataset : ", ds)
    # 텍스트 파일에서 데이터 읽어오기
    arr = read_list_from_txt(f"../dataset/real/{ds}.txt")
    n = len(arr)

    # ds가 예: "1K_random" → prefix = "1K"
    #         "100K_reverse_sorted" → prefix = "100K"
    size_prefix = ds.split("_")[0]  # "1K", "10K", "100K", "1M" etc.

    # 현재 데이터셋에 대한 결과를 담을 딕셔너리
    ds_result = {}

    # 12개 알고리즘 실행
    for algo_name, algo_func in algo_dict.items():
        print("current algorithm - ", algo_name)

        # 1M 데이터이면서 O(n^2) 알고리즘이면 건너뛰기
        if size_prefix == "1M" and (algo_name in n2_algos):
            continue

        times = []
        repeat = 50
        if size_prefix == '1M':
            repeat = 10
        if size_prefix == "100K":
            repeat = 10    
        if size_prefix == "100K" and (algo_name in n2_algos):
            repeat = 1
        

        try:
            for i in range(repeat):
                print(i)
                arr_copy = arr[:]
                start_time = time.time()
                algo_func(arr_copy)
                end_time = time.time()
                times.append(end_time - start_time)

            avg_time = sum(times) / len(times)
            ds_result[algo_name] = avg_time
        
        except Exception as e:
            print(f"Error in {algo_name} on dataset {ds}: {e}")

    # 이 데이터셋에 대한 결과 저장
    all_results[ds] = ds_result

    # 5) all_results를 파일에 저장
    with open("../test_result/results_3.json", "w") as f:
        json.dump(all_results, f, indent=4)

print("All experiments completed. Results saved to results.txt.")