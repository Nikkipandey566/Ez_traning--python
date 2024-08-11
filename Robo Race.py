a,b,c,d=list(map(int,input().split(" ")))
if a>c:
    a,c=c,a
    b,d=d,b
ans=c-a
pos=0
for pos in range (b):
    if(ans%b + pos*d)%b==0:
        break
if pos!=b:
    print(c+pos*d)
