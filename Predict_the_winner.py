import math
x=int(input())
l=list(map(int,input().split()))
k=0
s=0
for i in range(len(l)):
    if i%2==0:
        k+=l[i]
    else:
        s+=l[i]
z=abs(k-s)
if z%4==0:
    print("X")
else:
    print("Y")