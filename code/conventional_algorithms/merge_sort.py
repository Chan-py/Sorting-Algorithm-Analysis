def run(arr):
    arr_ = arr[:]
    n = len(arr_)
    # merge_sort(arr_, 0, n-1)
    merge_sort_3(arr_, 0, n-1)
    return arr_


def merge_sort(arr, p, r):
    if r - p < 1:
        return

    mid = (p+r) // 2
    merge_sort(arr, p, mid)
    merge_sort(arr, mid + 1, r)

    # merge_with_no_sentinel(arr, p, mid, r)
    merge(arr, p, mid, r)

def merge_sort_without_sentinel(arr, p, r):
    if r - p < 1:
        return

    mid = (p+r) // 2
    merge_sort(arr, p, mid)
    merge_sort(arr, mid + 1, r)

    merge_with_no_sentinel(arr, p, mid, r)
    # merge(arr, p, mid, r)


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

def merge_with_no_sentinel(arr, p, q, r):
    n1 = q - p + 1
    n2 = r - q

    L = []; R = []
    for i in range(n1):
        L.append(arr[p+i])
    for i in range(n2):
        R.append(arr[q+i+1])

    i, j = 0, 0
    k = p

    while i < len(L) and j < len(R):
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    if i < len(L):
        for x in range(i, len(L)):
            arr[k] = L[x]
            k += 1
    if j < len(R):
        for x in range(j, len(R)):
            arr[k] = R[x]
            k += 1


def merge_sort_3(arr, p, r):
    if p >= r:
        return

    m1 = p + (r - p) // 3
    m2 = p + 2 * (r - p) // 3 + 1

    merge_sort_3(arr, p, m1)
    merge_sort_3(arr, m1 + 1, m2 - 1)
    merge_sort_3(arr, m2, r)

    merge3(arr, p, m1, m2, r)


def merge3(arr, p, m1, m2, r):
    n1 = m1 - p + 1
    L = []
    for i in range(n1):
        L.append(arr[p + i])
    L.append(int(1e9))  # sentinel

    n2 = m2 - (m1 + 1)
    M = []
    for i in range(n2):
        M.append(arr[m1 + 1 + i])
    M.append(int(1e9))  # sentinel

    n3 = r - m2 + 1
    R = []
    for i in range(n3):
        R.append(arr[m2 + i])
    R.append(int(1e9))  # sentinel

    i = j = k = 0
    for l in range(p, r + 1):
        if L[i] <= M[j] and L[i] <= R[k]:
            arr[l] = L[i]
            i += 1
        elif M[j] <= R[k]:
            arr[l] = M[j]
            j += 1
        else:
            arr[l] = R[k]
            k += 1