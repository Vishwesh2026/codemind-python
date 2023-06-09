import math
x=int(input())
l=list(map(int,input().split()))
z=0
for i in range(x):
    if l[i]==1:
        z=z+l[i]
    for j in range(1,l[i]):
        if j*j==l[i]:
            z=z+l[i]
print(z)