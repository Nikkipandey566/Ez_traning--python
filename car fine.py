date=int(input())
n=int(input())
if n==0:
    print(-1)
else:
    car=list(map(int,input().split()))
    fine=0
    if date%2==0:
        for car in car:
            if car%2!=0:
                fine+=250
    else:
        for car in cars:
            if car%2==0:
                fine+=250
    print(fine)
