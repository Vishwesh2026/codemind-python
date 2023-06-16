x=int(input())
l=list(map(int,input().split()))
a,b=map(int,input().split())
k=0
for i in range(len(l)):
    if l[i]>=a and l[i]<=b:
        continue
    else:
        k=k+l[i]
print(k)