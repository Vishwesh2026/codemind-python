def find_last_even_number(arr):
    last_even_number = None

    for num in arr:
        if num % 2 == 0:
            last_even_number = num

    return last_even_number

N = int(input())
arr = list(map(int, input().split()))
last_even_number= find_last_even_number(arr)
print(last_even_number)
