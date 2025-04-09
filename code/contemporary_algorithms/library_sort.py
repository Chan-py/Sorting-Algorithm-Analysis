def run(arr):
    arr_ = arr[:]
    # return test_sort(arr_)
    return library_sort(arr_)

def library_sort(arr, epsilon=0.5):
    n = len(arr)
    
    S_size = int((2 + 2 * epsilon) * n)
    S = [None] * S_size
    
    S[0] = arr[0]
    positions = [0]
    
    m = 1
    
    while m < n:
        next_m = min(2 * m, n)
        for i in range(m, next_m):
            attempt_insert(S, positions, arr[i])
        
        new_active_length = int((2 + 2 * epsilon) * next_m)
        S, positions = rebalance(S, positions, next_m, new_active_length)
        m = next_m
    
    result = []
    for i in range(len(S)):
        if S[i] is not None:
            result.append(S[i])
    return result

def attempt_insert(S, positions, key):
    pos_index = binary_search_positions(S, positions, key)
    
    insert_idx = find_insert_pos(positions, pos_index)
    
    if 0 <= insert_idx < len(S) and S[insert_idx] is None:
        S[insert_idx] = key
    else:
        pos = insert_idx
        while pos < len(S) and S[pos] is not None:
            pos += 1
        
        for i in range(pos, insert_idx, -1):
            S[i] = S[i - 1]
        for i in range(len(positions)):
            if positions[i] >= insert_idx and positions[i] <= pos:
                positions[i] += 1
        S[insert_idx] = key
    
    insert_in_list(positions, pos_index, insert_idx)

def binary_search_positions(S, positions, key):
    l, r = 0, len(positions)
    while l < r:
        mid = (l + r) // 2
        if S[positions[mid]] <= key:
            l = mid + 1
        else:
            r = mid
    return l

def find_insert_pos(positions, pos_index):
    if pos_index == 0:
        return 0
    else:
        return positions[pos_index-1] + 1

def rebalance(S, positions, m, new_active_length):
    new_S = [None] * len(S)
    new_positions = []
    
    spacing = new_active_length / float(m)
    
    for i in range(m):
        old_idx = positions[i]
        val = S[old_idx]

        place_index = int((i + 0.5) * spacing)
        if place_index >= len(new_S):
            place_index = len(new_S) - 1

        new_S[place_index] = val
        new_positions.append(place_index)
    
    return new_S, new_positions



def test_sort(arr):
    result = [arr[0]]
    for i in range(1, len(arr)):
        pos = test_binary_search(result, arr[i])
        insert_in_list(result, pos, arr[i])
    return result

def test_binary_search(arr, key):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1
    return low

def insert_in_list(lst, insert_index, value):
    lst.append(None)
    for i in range(len(lst) - 1, insert_index, -1):
        lst[i] = lst[i - 1]
    lst[insert_index] = value