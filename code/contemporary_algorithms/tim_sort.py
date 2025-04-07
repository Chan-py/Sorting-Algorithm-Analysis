def run(arr):
    arr_ = arr[:]
    timsort(arr_)
    return arr_

def binary_search(arr, left, right, key):
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] > key:
            right = mid - 1
        else:
            left = mid + 1
    return left

def insertion_sort_binary(arr, left, right):
    for i in range(left + 1, right + 1):
        key = arr[i]
        pos = binary_search(arr, left, i - 1, key)
        for j in range(i - 1, pos - 1, -1):
            arr[j + 1] = arr[j]
        arr[pos] = key
    return arr

def merge(arr, p, q, r):
    n1 = q - p + 1
    n2 = r - q

    L = []; R = []
    for i in range(n1):
        L.append(arr[p+i])
    L.append(int(1e9))
    for i in range(n2):
        R.append(arr[q+i+1])
    R.append(int(1e9))

    i, j = 0, 0

    for k in range(p, r+1):
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1

def timsort(arr):
    n = len(arr)
    if n <= 1:
        return 

    runs = []
    run_start = 0

    for i in range(1, n):
        if arr[i] < arr[i - 1]:
            runs.append((run_start, i - 1))
            run_start = i
        
        if i == n - 1:
            runs.append((run_start, i))
    
    for (start, end) in runs:
        insertion_sort_binary(arr, start, end)
    
    size = len(runs)
    while size > 1:
        merged_runs = []
        i = 0
        while i < size:
            if i == size - 1:
                merged_runs.append(runs[i])
            else:
                left_start, left_end = runs[i]
                right_start, right_end = runs[i + 1]
                merge(arr, left_start, left_end, right_end)
                merged_runs.append((left_start, right_end))
                i += 1
            i += 1
        runs = merged_runs
        size = len(runs)
