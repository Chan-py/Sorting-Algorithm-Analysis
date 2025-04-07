def run(arr):
    return cocktail_shaker_sort(arr)

def cocktail_shaker_sort(arr):
    a = arr[:]
    n = len(a)
    start, end = 0, n - 1
    swapped = True
    while swapped:
        swapped = False
        for i in range(start, end):
            if a[i] > a[i+1]:
                a[i], a[i+1] = a[i+1], a[i]
                swapped = True
        if not swapped:
            break
        end -= 1
        swapped = False
        for i in range(end, start, -1):
            if a[i] < a[i-1]:
                a[i], a[i-1] = a[i-1], a[i]
                swapped = True
        start += 1
    return a