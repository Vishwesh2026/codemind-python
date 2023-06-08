def prime(x):
    c=0
    for i in range(1,x+1):
        if x%i==0:#checking whether the given number is prime or not
            c=c+1
    if c==2:
        return 1# if it is a prime number
    else:
        return 0
x=int(input())
temp=x
k=prime(x)
n=0 #total number of digits in given number
p=0 #total number of prime number or digit in the given number
if k==1:
    while temp:
        d=temp%10
        temp=temp//10
        n=n+1
        z=prime(d)
        if z==1:
            p=p+1
    if n==p:#If number of prime digits in the given number is same as the number of divisons
        print("Mega Prime")
    else:
        print("Not Mega Prime")
else:
    print("Not Mega Prime")
