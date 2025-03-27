import argparse

from sorters import bubble_sort, quick_sort
import time

def read_list_from_txt(filepath):
    with open(filepath, 'r') as f:
        data = f.read().split()
        data = list(map(int, data))
    return data

parser = argparse.ArgumentParser()
parser.add_argument("--algorithm", type=str, default="bubble",
                    help="sorting algorithm")
parser.add_argument("--list", type=str, default="dataset/test/list.txt",
                    help="testcase file")
args = parser.parse_args()

data = read_list_from_txt(args.list)
print("Original list:", data)

if args.algorithm == "bubble":
    sorted_data = bubble_sort(data[:])
elif args.algorithm == "quick":
    sorted_data = quick_sort(data[:])
else:
    raise ValueError(f"지원하지 않는 알고리즘입니다: {args.algorithm}")

print("Sorted list:", sorted_data)