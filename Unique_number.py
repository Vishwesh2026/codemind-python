x=int(input())
s=[]
k=str(x)
h=len(k)
for i in k:
   if i not in s:
       s.append(i)
if len(s)==h:
    print("Unique Number")
else:
    print("Not Unique Number")