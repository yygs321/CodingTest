n=int(input())
a=list(map(int,input().split()))
M=max(a)
b=0
for i in range(n):
    a[i] = a[i]/M*100
    b=b+a[i]
b=b/n
print(b)