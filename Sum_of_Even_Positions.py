n=int(input())
arr=list(map(int,input().strip().split()))
sumEven=0
for i in range(0,len(arr),2):
    sumEven+=arr[i]
print(sumEven)