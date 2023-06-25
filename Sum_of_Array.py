n=int(input())
arr=list(map(int,input().strip().split()))
sum_arr=0
for i in range(0,len(arr)):
        sum_arr+=arr[i]
print(sum_arr)