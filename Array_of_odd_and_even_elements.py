def odd_even_array(arr):
    even = []
    odd = []
    for num in arr:
        if num % 2 != 0:
            odd.append(num)
        else:
            even.append(num)
    if not odd:
        return even
    elif not even:
        return odd
    else:
        return odd + even

N = int(input())
array = list(map(int, input().split()))
result = odd_even_array(array)
print(*result)
