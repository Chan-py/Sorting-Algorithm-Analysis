def run(arr):
    arr_ = arr[:]
    timsort(arr_)
    return arr_

def timsort(arr):
    n = len(arr)
    if n <= 1:
        return

    min_run = calc_min_run(n)
    runs = []
    i = 0

    while i < n:
        run_start = i
        i += 1
        
        if i < n:
            if arr[i] < arr[i - 1]:
                while i < n and arr[i] <= arr[i - 1]:
                    i += 1
                arr[run_start:i] = arr[run_start:i][::-1]
            else:
                while i < n and arr[i] >= arr[i - 1]:
                    i += 1
        
        run_end = i - 1
        run_len = run_end - run_start + 1
        
        if run_len < min_run:
            end = min(run_start + min_run - 1, n - 1)
            insertion_sort(arr, run_start, end)
            run_end = end
            i = end + 1
        
        runs.append((run_start, run_end))
    
    size = len(runs)
    while size > 1:
        merged_runs = []
        i = 0
        while i < size:
            if i == size - 1:
                merged_runs.append(runs[i])
                i += 1
            else:
                left_start, left_end = runs[i]
                right_start, right_end = runs[i + 1]
                merge(arr, left_start, left_end, right_end)
                merged_runs.append((left_start, right_end))
                i += 2
        runs = merged_runs
        size = len(runs)

def insertion_sort(arr, left, right):
    for i in range(left + 1, right + 1):
        key = arr[i]
        j = i - 1
        # 배열의 [left .. (i-1)] 구간에서 key의 위치를 찾는다
        while j >= left and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

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

def calc_min_run(n):
    r = 0
    while n >= 64:
        r |= n & 1
        n //= 2
    return n + r
