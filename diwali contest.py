n=int(input())
p=int(input())
x=240-p
c=0
for i in range(1,n+1):
    if x>0 and x>i*5:
        x=x-(i*5)
        c=c+1
    else:
        break
print(c)
