#n개의 집, m개 간선, 가중치 o 
#마을이 서로 연결되도록 분할

n,m=map(int,input().split())
load=[]
for i in range(m):
    s,e,v=map(int,input().split())
    load.append((s,e,v))
load.sort(key=lambda x:x[2])

root=[i for i in range(n+1)]
def union(x,y):
    xroot=find(x)
    yroot=find(y)
    if xroot<yroot:
        root[yroot]=xroot
    else:
        root[xroot]=yroot

def find(x):
    if root[x]!=x:
        root[x]=find(root[x])
    return root[x]

result=0
last=0
for ld in load:
    s,e,v=ld
    if find(s)!=find(e):
        union(s,e)
        result+=v
        last=v

print(result-last)