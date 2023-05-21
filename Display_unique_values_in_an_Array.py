x=int(input())
l=list(map(int,input().split()))
x=0
for i in l:
    k=l.count(i)
    if(k==1):
        x+=1
        print(i,end=" ")
if(x==0):
    print("-1")