n=int(input())
k=n*n
s=0
while k:
    d=k%10
    k=k//10
    s=s+d
if s==n:
    print("Neon Number")
else:
    print("Not Neon Number")