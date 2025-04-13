import argparse
import time
from conventional_algorithms import merge_sort, heap_sort, bubble_sort, insertion_sort, selection_sort, quick_sort
from contemporary_algorithms import library_sort, tim_sort, cocktail_shaker_sort, comb_sort, tournament_sort, intro_sort
from utils import check_sorted, read_list_from_txt

parser = argparse.ArgumentParser()
parser.add_argument("--algorithm", type=str, default="merge",
                    help="sorting algorithm")
parser.add_argument("--list", type=str, default="../dataset/real/100K_reverse_sorted.txt",
                    help="testcase file")
args = parser.parse_args()

data = read_list_from_txt(args.list)

# print("Original list:", data)

if args.algorithm == "stl":
    start_time = time.time()
    sorted_data = sorted(data[:])
    end_time = time.time()
    print(end_time - start_time)
elif args.algorithm == "merge":
    start_time = time.time()
    sorted_data = merge_sort.run(data[:])
    end_time = time.time()
    print(end_time - start_time)
    check_sorted(sorted_data)
elif args.algorithm == "heap":
    start_time = time.time()
    sorted_data = heap_sort.run(data[:])
    end_time = time.time()
    print(end_time - start_time)
    check_sorted(sorted_data)
elif args.algorithm == "bubble":
    start_time = time.time()
    sorted_data = bubble_sort.run(data[:])
    end_time = time.time()
    print(end_time - start_time)
    check_sorted(sorted_data)
elif args.algorithm == "insertion":
    start_time = time.time()
    sorted_data = insertion_sort.run(data[:])
    end_time = time.time()
    print(end_time - start_time)
    check_sorted(sorted_data)
elif args.algorithm == "selection":
    start_time = time.time()
    sorted_data = selection_sort.run(data[:])
    end_time = time.time()
    print(end_time - start_time)
    check_sorted(sorted_data)
elif args.algorithm == "quick":
    start_time = time.time()
    sorted_data = quick_sort.run(data[:])
    end_time = time.time()
    print(end_time - start_time)
    check_sorted(sorted_data)
elif args.algorithm == "library":
    start_time = time.time()
    sorted_data = library_sort.run(data[:])
    end_time = time.time()
    print(end_time - start_time)
    check_sorted(sorted_data)
elif args.algorithm == "tim":
    start_time = time.time()
    sorted_data = tim_sort.run(data[:])
    end_time = time.time()
    print(end_time - start_time)
    check_sorted(sorted_data)
elif args.algorithm == "cocktail":
    start_time = time.time()
    sorted_data = cocktail_shaker_sort.run(data[:])
    end_time = time.time()
    print(end_time - start_time)
    check_sorted(sorted_data)
elif args.algorithm == "comb":
    start_time = time.time()
    sorted_data = comb_sort.run(data[:])
    end_time = time.time()
    print(end_time - start_time)
    check_sorted(sorted_data)
elif args.algorithm == "tournament":
    start_time = time.time()
    sorted_data = tournament_sort.run(data[:])
    end_time = time.time()
    print(end_time - start_time)
    check_sorted(sorted_data)
elif args.algorithm == "intro":
    start_time = time.time()
    sorted_data = intro_sort.run(data[:])
    end_time = time.time()
    print(end_time - start_time)
    check_sorted(sorted_data)
else:
    raise ValueError(f"지원하지 않는 알고리즘입니다: {args.algorithm}")

# print("Sorted list:", sorted_data)