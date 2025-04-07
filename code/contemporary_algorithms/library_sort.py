import random
import bisect
import math

def run(arr):
    return library_sort(arr)

def library_sort(arr, epsilon=0.5):
    n = len(arr)
    if n == 0:
        return []
    A = arr[:]
    random.shuffle(A)
    m = 1
    size = int((1 + epsilon) * m) + 1
    S = [None] * size
    pos_list = []
    sorted_vals = []
    mid = size // 2
    S[mid] = A[0]
    pos_list.append(mid)
    sorted_vals.append(A[0])
    i = 1
    while i < n:
        round_inserts = min(m, n - i)
        for _ in range(round_inserts):
            x = A[i]
            i += 1
            idx = bisect.bisect_left(sorted_vals, x)
            if idx == 0:
                base = pos_list[0]
                gap_found = False
                for j in range(base - 1, -1, -1):
                    if S[j] is None:
                        pos = j
                        gap_found = True
                        break
                if not gap_found:
                    for j in range(base + 1, size):
                        if S[j] is None:
                            pos = j
                            gap_found = True
                            break
                if not gap_found:
                    raise Exception("Gap not found")
            elif idx == len(sorted_vals):
                base = pos_list[-1]
                gap_found = False
                for j in range(base + 1, size):
                    if S[j] is None:
                        pos = j
                        gap_found = True
                        break
                if not gap_found:
                    for j in range(base - 1, -1, -1):
                        if S[j] is None:
                            pos = j
                            gap_found = True
                            break
                if not gap_found:
                    raise Exception("Gap not found")
            else:
                left_bound = pos_list[idx - 1]
                right_bound = pos_list[idx]
                pos = None
                for j in range(left_bound + 1, right_bound):
                    if S[j] is None:
                        pos = j
                        break
                if pos is None:
                    for j in range(right_bound, size):
                        if S[j] is None:
                            pos = j
                            break
                    if pos is None:
                        for j in range(left_bound, -1, -1):
                            if S[j] is None:
                                pos = j
                                break
                    if pos is None:
                        raise Exception("Gap not found")
            S[pos] = x
            bisect.insort(pos_list, pos)
            sorted_vals.insert(bisect.bisect_left(sorted_vals, x), x)
        m = len(sorted_vals)
        if i < n:
            new_size = int((2 + 2 * epsilon) * m) + 1
            new_S = [None] * new_size
            new_pos_list = []
            gap = new_size / m
            for k in range(m):
                new_index = int(round(gap / 2 + k * gap))
                new_S[new_index] = sorted_vals[k]
                new_pos_list.append(new_index)
            S = new_S
            pos_list = new_pos_list
            size = new_size
    return sorted_vals