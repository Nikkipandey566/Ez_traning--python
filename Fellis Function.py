n=int(input())
f=[1,1]
for i in range(2,n+1):
    b=(f[i-1]+7*f[i-1]+(i//4))%(10**9+7)
    f.append(b)
print(f[n])
