def find_last_odd_number(arr):
    last_odd_number = None

    for num in arr:
        if num % 2 != 0:
            last_odd_number = num

    return last_odd_number

N = int(input())
arr = list(map(int, input().split()))
last_odd_number= find_last_odd_number(arr)
print(last_odd_number)
