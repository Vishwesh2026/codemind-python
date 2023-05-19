x=int(input())
y=int(input())
for i in range(x,y+1):
    temp=i
    while temp!=0:
        d=temp%10
        if d==0 or i%d!=0:
            break
        temp=temp//10
    if temp==0:
        print(i,end=" ")