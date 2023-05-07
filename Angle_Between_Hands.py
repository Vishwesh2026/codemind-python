hour,minutes=map(int,input("").split(":"))
if hour>12:     #Converting digital to analog..!
    hour-=12
angle=min(abs(((11/2)*minutes)-(30*hour)),360-abs(((11/2)*minutes)-(30*hour)))
print(angle)