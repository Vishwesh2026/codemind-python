def count_odd_between_odd(arr):
    count = 0
    for i in range(1, len(arr)-1):
        if arr[i-1] % 2 == 0 and arr[i+1] % 2 == 0 and arr[i] % 2 == 0:
            count += 1
    return count

# Read the input
N = int(input())
arr = list(map(int, input().split()))

# Call the function and print the result
result = count_odd_between_odd(arr)
print(result)
