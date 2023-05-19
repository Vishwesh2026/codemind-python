x=int(input())
a=0
b=1
for i in range(x):
    c=a+b
    a=b
    b=c
    if c>x:
        if(abs(x-c)==abs(x-a)):
            print(a,c)
            break
        elif(abs(x-c)>abs(x-a)):
            print(a)
            break
        else:
            print(c)
            break