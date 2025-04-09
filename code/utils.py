def check_sorted(arr):
    n = len(arr)
    for i in range(n-1):
        if arr[i] > arr[i+1]:
            print(arr[i], arr[i+1])
            print("Wrong")
            return False
    print("Right")
    return True

def read_list_from_txt(filepath):
    with open(filepath, 'r') as f:
        data = f.read().split()
        data = list(map(int, data))
    return data