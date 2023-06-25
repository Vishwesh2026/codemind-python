n=int(input())
arr=list(map(int,input().strip().split()))
sumOdd=0
for i in range(0,len(arr)):
    if arr[i]%2 !=0:
        sumOdd+=arr[i]
print(sumOdd)