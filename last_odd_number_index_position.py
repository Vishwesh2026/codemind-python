def find_last_odd_index(arr):
    last_odd_index = -1
    for i in range(len(arr)):
        if arr[i] % 2 != 0:
            last_odd_index = i
    return last_odd_index

N = int(input())
arr = list(map(int, input().split()))
last_odd_index = find_last_odd_index(arr)
print(last_odd_index)
