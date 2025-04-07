import random

def run(arr):
    arr_ = arr[:]
    # quick_sort(arr_, 0, len(arr_) - 1)
    dual_pivot_quick_sort(arr_, 0, len(arr_) - 1)
    return arr_

def quick_sort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quick_sort(A, p, q-1)
        quick_sort(A, q+1, r)

def partition(A, p, r):
    x = A[r]
    i = p-1
    for j in range(p, r):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[r] = A[r], A[i+1]
    return i+1


def randomized_quick_sort(A, p, r):
    if p < r:
        q = randomized_partition(A, p, r)
        randomized_quick_sort(A, p, q-1)
        randomized_quick_sort(A, q+1, r)

def randomized_partition(A, p, r):
    i = random.randint(p, r)
    A[r], A[i] = A[i], A[r]
    return partition(A, p, r)



def dual_pivot_quick_sort(A, low, high):
    if low < high:
        p, q = dual_pivot_partition(A, low, high)
        dual_pivot_quick_sort(A, low, p - 1)
        dual_pivot_quick_sort(A, p + 1, q - 1)
        dual_pivot_quick_sort(A, q + 1, high)

def dual_pivot_partition(A, low, high):
    if A[low] > A[high]:
        A[low], A[high] = A[high], A[low]
    pivot1 = A[low]
    pivot2 = A[high]

    lt = low + 1
    gt = high - 1
    i = low + 1

    while i <= gt:
        if A[i] < pivot1:
            A[i], A[lt] = A[lt], A[i]
            lt += 1
            i += 1
        elif A[i] > pivot2:
            A[i], A[gt] = A[gt], A[i]
            gt -= 1
        else:
            i += 1

    A[low], A[lt - 1] = A[lt - 1], A[low]
    A[high], A[gt + 1] = A[gt + 1], A[high]

    return lt - 1, gt + 1



def quick_sort_DS(arr, left, right):
    if left < right:
        i = left
        j = right + 1
        pivot = arr[left]

        while True:
            i += 1
            while i <= right and arr[i] < pivot:
                i += 1

            j -= 1
            while j >= left and arr[j] > pivot:
                j -= 1

            if i >= j:
                break
            arr[i], arr[j] = arr[j], arr[i]

        arr[left], arr[j] = arr[j], arr[left]

        quick_sort(arr, left, j - 1)
        quick_sort(arr, j + 1, right)