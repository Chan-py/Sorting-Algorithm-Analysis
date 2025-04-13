def run(arr):
    arr_ = arr[:]
    return tournament_sort(arr_)

def tournament_sort(arr):
    n = len(arr)
    m = 1
    while m < n:
        m *= 2
    tree = [None] * (2 * m)

    for i in range(m, m + n):
        tree[i] = (arr[i - m], i - m)
    for i in range(m + n, 2 * m):
        tree[i] = (float('inf'), -1)

    for i in range(m - 1, 0, -1):
        left = tree[2 * i]
        right = tree[2 * i + 1]
        tree[i] = left if left[0] <= right[0] else right

    result = []
    for _ in range(n):
        winner = tree[1]
        result.append(winner[0])
        pos = winner[1] + m
        tree[pos] = (float('inf'), winner[1])
        pos //= 2
        while pos >= 1:
            left = tree[2 * pos]
            right = tree[2 * pos + 1]
            tree[pos] = left if left[0] <= right[0] else right
            pos //= 2
    return result