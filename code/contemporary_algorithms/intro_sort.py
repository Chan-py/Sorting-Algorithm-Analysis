import math
import heapq

def run(arr):
    return intro_sort(arr)

def intro_sort(arr, reverse=False):
    # 비교 함수: reverse가 False이면 오름차순, True이면 내림차순
    def compare(a, b):
        return a > b if reverse else a < b

    # Insertion Sort: subarr[left:right+1]를 제자리 정렬
    def insertion_sort(subarr, left, right):
        for i in range(left + 1, right + 1):
            key = subarr[i]
            j = i - 1
            while j >= left and compare(key, subarr[j]):
                subarr[j + 1] = subarr[j]
                j -= 1
            subarr[j + 1] = key

    # Heap Sort: subarr[left:right+1]를 힙 정렬로 정렬
    def heap_sort(subarr, left, right):
        # Python의 heapq는 최소 힙이므로, 오름차순 정렬은 그대로, 내림차순은 부호 반전하여 처리
        sub = subarr[left:right + 1]
        if reverse:
            # 내림차순: 음수로 만들어 정렬한 후 다시 원래 값 복원
            sub = [-x for x in sub]
            heapq.heapify(sub)
            sorted_sub = [-heapq.heappop(sub) for _ in range(len(sub))]
        else:
            heapq.heapify(sub)
            sorted_sub = [heapq.heappop(sub) for _ in range(len(sub))]
        subarr[left:right + 1] = sorted_sub

    # Quick Sort: subarr[left:right]를 재귀적으로 정렬, depth가 0이면 힙 정렬로 전환
    # 여기서 left와 right는 배열의 인덱스(양쪽 포함)
    def quick_sort(subarr, left, right, depth):
        if left >= right:
            return
        if depth == 0:
            if (right - left + 1) > 16:
                heap_sort(subarr, left, right)
            return
        pivot = subarr[(left + right) // 2]
        i, j = left, right
        while i <= j:
            while i <= right and compare(subarr[i], pivot):
                i += 1
            while j >= left and not compare(subarr[j], pivot):
                j -= 1
            if i <= j:
                subarr[i], subarr[j] = subarr[j], subarr[i]
                i += 1
                j -= 1
        if left < j:
            quick_sort(subarr, left, j, depth - 1)
        if i < right:
            quick_sort(subarr, i, right, depth - 1)

    n = len(arr)
    # 배열 길이가 짧으면 바로 삽입 정렬
    if n <= 16:
        insertion_sort(arr, 0, n - 1)
        return arr

    # 재귀 깊이 제한: 2 * ceil(log2(n))
    depth_limit = 2 * math.ceil(math.log2(n))
    quick_sort(arr, 0, n - 1, depth_limit)
    # 마지막으로 전체 배열에 대해 삽입 정렬로 마무리
    insertion_sort(arr, 0, n - 1)
    return arr