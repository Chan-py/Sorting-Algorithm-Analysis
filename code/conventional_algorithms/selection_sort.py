def run(arr):
    arr_ = arr[:]
    n = len(arr_)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr_[j] < arr_[min_idx]:
                min_idx = j
        arr_[i], arr_[min_idx] = arr_[min_idx], arr_[i]
    return arr_