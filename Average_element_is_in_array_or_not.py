N = int(input())
array = list(map(int, input().split()))

average = sum(array) // N

if average in array:
    print("True")
else:
    print("False")