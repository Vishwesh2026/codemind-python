def find_Last_even_element_index(arr):
    Last_even_element_index = -1
    for i in range(len(arr)):
        if arr[i] % 2 == 0:
            Last_even_element_index = i
    return Last_even_element_index

N = int(input())
arr = list(map(int, input().split()))
Last_even_element_index = find_Last_even_element_index(arr)
print(Last_even_element_index)
