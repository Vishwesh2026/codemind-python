x=int(input())
l=list(map(int,input().split()))
k=0
s=0
for i in range(len(l)):
    if i%2==0:
        k=k+l[i]
    else:
        s=s+l[i]
a=abs(s-k)
if(a==0):
    print("YES")
else:
    print("NO")