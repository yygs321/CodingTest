n,m,k=map(int,input().split())
money=list(map(int,input().split()))
money.insert(0,0)
root=[i for i in range(n+1)]

def union(x,y):
    xroot=find(x)
    yroot=find(y)
    if money[xroot]<money[yroot]:
        root[yroot]=xroot
        money[yroot]=money[xroot]
    else:
        root[xroot]=yroot
        money[xroot]=money[yroot]

def find(x):
    if root[x]!=x:
        root[x]=find(root[x])
    return root[x]

for i in range(m):
    x,y=map(int,input().split())
    union(x,y)

result=0
for i in range(1,n+1):
    if root[i]==i:
        result+=money[i]

if result>k or result==0:
    print("Oh no")
else:
    print(result)