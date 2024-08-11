#REDUCE TILL ZERO:-

x=int(input())
y=int(input())
while y>0:
    if x<y:
        x,y=y,x
    else:
        x,y=y,x-y
print(x)
