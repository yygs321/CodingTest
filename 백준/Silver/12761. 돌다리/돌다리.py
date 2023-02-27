#a,b 스카이 콩콩
#위치 n,m
from collections import deque
a,b,n,m=map(int,input().split())
lst=[1,-1,a,-a,b,-b,a,b]
visited=[0 for _ in range(100001)]
queue=deque()

def bfs(n):
    queue.append(n)
    
    while queue:
        q=queue.popleft()
        if(q==m):
            return
        
        for idx, ls in enumerate(lst):
            if idx>=6 and q*ls<=100000:
                 if visited[q*ls]==0:
                    visited[q*ls]=visited[q]+1
                    queue.append(q*ls)
                    continue
                
            if 0<= q+ls<=100000:
                if visited[q+ls]==0:
                    visited[q+ls]=visited[q]+1
                    queue.append(q+ls)
                
bfs(n)
print(visited[m])