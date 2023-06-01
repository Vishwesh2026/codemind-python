x=int(input())
l=list(map(int,input().split()))
c=0
z=0
for i in l:
    k=l.count(i)
    if k==1:
        c=c+1
        if i>z:
            z=i
if c==0:
    print("-1")
else:
    print(z)