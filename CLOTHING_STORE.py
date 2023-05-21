x=int(input())
l=list(map(int,input().split()))
s=set(l)
k=0
for i in s:
    if l.count(i)%2==0:
        k+=l.count(i)//2
    elif l.count(i)%2==1:
        k+=l.count(i)//2
print(k)
        