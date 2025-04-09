def run(arr):
    arr_ = arr[:]
    return cocktail_shaker_sort(arr_)

def cocktail_shaker_sort(arr):
    n = len(arr)
    start, end = 0, n - 1
    swapped = True
    while swapped:
        swapped = False
        for i in range(start, end):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                swapped = True
        if not swapped:
            break
        end -= 1
        swapped = False
        for i in range(end, start, -1):
            if arr[i] < arr[i-1]:
                arr[i], arr[i-1] = arr[i-1], arr[i]
                swapped = True
        start += 1
    return arr