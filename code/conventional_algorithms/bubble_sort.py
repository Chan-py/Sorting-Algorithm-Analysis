def run(arr):
    arr_ = arr[:]
    n = len(arr_)
    for i in range(n):
        for j in range(n - i - 1):
            if arr_[j] > arr_[j+1]:
                arr_[j], arr_[j+1] = arr_[j+1], arr_[j]
    return arr_