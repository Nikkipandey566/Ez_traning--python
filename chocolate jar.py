choco_jar=list(map(int,input().split()))
n=int(input())
count=0
for i in choco_jar:
    if i%3==0:
        count +=(i//3)
    elif i%3!=0:
        count+=(i//3)+1
print(count)
