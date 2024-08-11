N,M=list(map(int,input().split(" ")))
arr=list(map(int,input().split(" ")))
products=[]
for i in range(M):
    price,weight=list(map(int,input().split(" ")))
    products.append([price,weight])
ans=[]
for person in arr:
    total=0
    for prc,wt in products:
        if prc<=person:
            total+=wt
    ans.append(total)
print(*ans, sep=" ")
