def calculate_absolute_difference(arr):
    sumEven = 0
    sumOdd = 0

    for i in range(0, len(arr), 2):
        sumEven += arr[i]

    for i in range(1, len(arr), 2):
        sumOdd += arr[i]

    absolute_difference = abs(sumEven - sumOdd)
    return absolute_difference
n=int(input())
arr=list(map(int,input().strip().split()))
result=calculate_absolute_difference(arr)
print(result)