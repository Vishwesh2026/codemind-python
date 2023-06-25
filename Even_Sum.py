n=int(input())
arr=list(map(int,input().strip().split()))
sumEven=0
for i in range(0,len(arr)):
    if arr[i]%2 ==0:
        sumEven+=arr[i]
print(sumEven)