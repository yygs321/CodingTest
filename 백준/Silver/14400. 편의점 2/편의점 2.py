n=int(input())
xlist=[]
ylist=[]
for _ in range(n):
    x,y=map(int,input().split())
    xlist.append(x)
    ylist.append(y)

xlist.sort()
ylist.sort()

midX=xlist[(n-1)//2]
midY=ylist[(n-1)//2]

dist=0
for i in range(n):
    dist+=abs(midX-xlist[i])+abs(midY-ylist[i])
    
print(dist)