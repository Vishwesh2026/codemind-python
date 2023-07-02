def even_odd_array(arr):
    even = []
    odd = []
    for num in arr:
        if num % 2 == 0:
            even.append(num)
        else:
            odd.append(num)
    if not even:
        return odd
    elif not odd:
        return even
    else:
        return even + odd

N = int(input())
array = list(map(int, input().split()))
result = even_odd_array(array)
print(*result)
