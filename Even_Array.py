n=int(input())
l=list(map(int,input().strip().split()))
c=0
for i in range(n):
    if l[i]%2==0:
        c=c+1
if c==n :
    print("True")
else :
    print("False")