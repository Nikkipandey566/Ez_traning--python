n=int(input())
arr=list(map(int,input().split()))
d={}
for num in arr:
    if num not in d:
        d[num]=1
    else:
        d[num]+=1
res=[]
for key,val in d.items():
    res=res+[val]*key
res.sort()
print(res)
