import math

def run(arr):
    arr_ = arr[:]
    return intro_sort(arr_)

def intro_sort(arr):
    n = len(arr)
    if n <= 16:
        insertion_sort_range(arr, 0, n - 1)
        return arr
    
    depth_limit = 2 * math.ceil(math.log2(n))
    quick_sort_range(arr, 0, n - 1, depth_limit)
    insertion_sort_range(arr, 0, n - 1)
    return arr

def insertion_sort_range(arr, left, right):
    for i in range(left + 1, right + 1):
        key = arr[i]
        j = i - 1
        while j >= left and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


def heap_sort_range(arr, left, right):
    subarr = arr[left:right+1]
    sorted_subarr = Heap_sort(subarr)
    arr[left:right+1] = sorted_subarr

# from heap_sort.py
def Heap_sort(arr):
    n = len(arr)
    Build_Max_Heap(arr, n)
    for i in range(n-1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        Max_Heapify(arr, i, 0)
    return arr

def Max_Heapify(A, n, i):
    left = 2*i + 1
    right = 2*i + 2
    largest = i
    if left < n and A[left] > A[largest]:
        largest = left
    if right < n and A[right] > A[largest]:
        largest = right
    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        Max_Heapify(A, n, largest)

def Build_Max_Heap(A, n):
    for i in range(n//2 - 1, -1, -1):
        Max_Heapify(A, n, i)


def quick_sort_range(arr, left, right, depth):
    if left < right:
        if depth == 0:
            if (right - left + 1) > 16:
                heap_sort_range(arr, left, right)
            else:
                insertion_sort_range(arr, left, right)
            return
        q = partition_range(arr, left, right)
        quick_sort_range(arr, left, q - 1, depth - 1)
        quick_sort_range(arr, q + 1, right, depth - 1)

def partition_range(arr, left, right):
    pivot = arr[right]
    i = left - 1
    for j in range(left, right):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[right] = arr[right], arr[i + 1]
    return i + 1
