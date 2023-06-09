x=int(input())
z=list(map(int,input().split()))
k=x//2
j=[]
for i in z[x:k-1:-1]:
    j.append(i)
for i in z[:k:]:
    j.append(i)
print(*j)
    