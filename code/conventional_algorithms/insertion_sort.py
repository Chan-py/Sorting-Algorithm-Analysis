def run(arr):
    arr_ = arr[:]
    return insertion_sort(arr_)

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr

def binary_search(arr, left, right, key):
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] > key:
            right = mid - 1
        else:
            left = mid + 1
    return left

def insertion_sort_binary(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        pos = binary_search(arr, 0, i - 1, key)
        
        for j in range(i - 1, pos - 1, -1):
            arr[j + 1] = arr[j]
        arr[pos] = key
    return arr

