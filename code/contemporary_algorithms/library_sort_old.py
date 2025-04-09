def run(arr):
    arr_ = arr[:]
    # return test_sort(arr_)
    return library_sort(arr_, 0.5)

def test_sort(arr):
    result = [arr[0]]
    for i in range(1, len(arr)):
        pos = test_binary_search(result, arr[i])
        result.append(None)
        for j in range(len(result) - 1, pos, -1):
            result[j] = result[j - 1]
        result[pos] = arr[i]
        # result.insert(pos, arr[i])
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

def binary_search_support(S, support_positions, key):
    """
    support_positions에 저장된 S의 값들(이미 삽입된 원소들)을 대상으로
    key가 들어갈 위치(삽입할 인덱스)를 이분 탐색으로 찾는다.
    """
    low = 0
    high = len(support_positions) - 1
    while low <= high:
        mid = (low + high) // 2
        if S[support_positions[mid]] < key:
            low = mid + 1
        else:
            high = mid - 1
    return low

def insert_into_S(S, support_positions, insert_index, key):
    """
    support_positions를 기준으로, key를 삽입할 적당한 gap(빈 칸)을 찾아 key를 삽입한다.
    목표 위치는 insert_index가 0이면 0, 
    그렇지 않으면 support_positions[insert_index-1]과 support_positions[insert_index] 사이의 중간값으로 정한다.
    만약 해당 위치가 이미 차 있다면 오른쪽으로 gap을 찾으며 밀어낸다.
    """
    check = False
    if insert_index == 0:
        pos = 0
    elif insert_index == len(support_positions):
        pos = support_positions[-1] + 1
    else:
        pos = support_positions[insert_index - 1] + 1
    while pos < len(S) and S[pos] is not None:
        pos += 1
    if pos < len(S):
        S[pos] = key
    else:
        raise Exception("No gap found in S for insertion")
    # print(S)
    # print(support_positions)
    # if check and pos >= support_positions[insert_index]:
    #     print("비사앙")
    return pos

def rebalance(S, support_positions, m, new_active_length):
    """
    현재 m개의 정렬된 원소(지원 원소들)가 S의 support_positions에 위치해 있다.
    이들을 새로운 active region(길이 new_active_length) 내에 고르게 분포시키도록 재배치한다.
    새로운 위치는 각 원소에 대해 (i + 0.5) * new_active_length/m 로 계산한다.
    """
    new_S = [None] * len(S)
    new_support_positions = []
    for i in range(m):
        new_pos = int((i + 0.5) * new_active_length / m)
        new_S[new_pos] = S[support_positions[i]]
        new_support_positions.append(new_pos)
    return new_S, new_support_positions

def library_sort(A, epsilon):
    """
    Library Sort 구현:
    
    - A의 n개 원소를 무작위 순서로 S에 삽입한다.
    - S는 여분 공간을 포함해 (2+2ε)*n 크기로 할당한다.
    - 삽입은 log n 라운드로 진행되며, 각 라운드마다 2^(i-1)개(즉, 전체의 절반씩)를
      새로운 원소(인터칼레이트 원소)로 삽입하고, 삽입은 지원 원소들의 위치를 기준으로 
      이분 탐색하여 수행한다.
    - 라운드가 끝나면, 현재 m개의 원소를 새로운 active region (길이 = (2+2ε)*m) 내에
      균등하게 재배치(리밸런스)한다.
    """
    import math
    n = len(A)
    # 최종 active region을 위한 충분한 공간 확보를 위해 S의 크기는 (2+2ε)*n로 할당
    S_size = int((2 + 2 * epsilon) * n)
    S = [None] * S_size

    # 첫 원소 삽입: m = 1일 때 active region은 (1+ε)*1, 여기서는 단순히 그 중간(혹은 0번 인덱스)에 삽입
    first_pos = int((1 + epsilon) / 2)
    S[first_pos] = A[0]
    support_positions = [first_pos]
    m = 1

    # 라운드 진행: 각 라운드마다 m을 두 배로 늘리며 (최대 n까지)
    while m < n:
        next_m = min(2 * m, n)
        # 현재 라운드 전 active region은 (1+ε)*m 길이 내에 위치
        for i in range(m, next_m):
            key = A[i]
            insert_index = binary_search_support(S, support_positions, key)
            pos = insert_into_S(S, support_positions, insert_index, key)

            support_positions.append(None)
            for i in range(len(support_positions) - 1, insert_index, -1):
                support_positions[i] = support_positions[i - 1]
            support_positions[insert_index] = pos

            # support_positions.insert(insert_index, pos)
        m = next_m
        # 라운드 종료 후, rebalance를 수행:
        # 재배치 후 active region 길이는 (2+2ε)*m로 정의됨.
        new_active_length = int((2 + 2 * epsilon) * m)
        S, support_positions = rebalance(S, support_positions, m, new_active_length)
    
    # 최종적으로 support_positions에 위치한 원소들이 정렬된 상태임.
    sorted_list = [S[i] for i in support_positions]
    return sorted_list