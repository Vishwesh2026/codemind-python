n=int(input())
arr=list(map(int,input().strip().split()))
sumOdd=0
for i in range(1,len(arr),2):
    sumOdd+=arr[i]
print(sumOdd)