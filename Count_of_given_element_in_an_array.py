def appearence(l,z):
    c=0
    for i in range(len(l)):
        if l[i]==z:
            c=c+1
    return c
            
n=int(input())
l=list(map(int,input().split()))
z=int(input())
result=appearence(l,z)
print(result)