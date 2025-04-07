def run(arr):
    arr_ = arr[:]
    Heap_sort(arr_)
    return arr_

def Heap_sort(arr):
    n = len(arr)
    Build_Max_Heap(arr, n)
    for i in range(n-1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        Max_Heapify(arr, i, 0)


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