def prime(i):
    for j in range(2,int(i**0.5+1)):
        if i%j==0:
            return 0
    else:
        return 1

x=int(input())
y=int(input())
z=x+y
for i in range(1,10):
    result=z+i
    if prime(result):
        print(i)
        break