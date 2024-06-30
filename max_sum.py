n=int(input())
arr=list(map(int,input().split()))
max_sum=-float("inf")
present_sum=0
for i in arr:
    present_sum+=i
    max_sum=max(max_sum,present_sum)
    if present_sum<0:
        present_sum=0
print(max_sum)
