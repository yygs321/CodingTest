#최소 칸수: bfs
from collections import deque

n,m=map(int,input().split())
map=[list(map(int,input().rstrip())) for _ in range(n)]
visited=[[0 for _ in range(m)] for _ in range(n)]

n-=1
m-=1
dx=[-1,1,0,0]
dy=[0,0,-1,1]
queue=deque()
answer=0

def bfs(r,c):
    global answer
    queue.append((r,c))
    visited[0][0]=1
  
    while queue:
        x,y=queue.popleft()
    
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
      
            if 0<=nx<=n and 0<=ny<=m:
                if map[nx][ny]==1 and visited[nx][ny]==0:
                    visited[nx][ny]=visited[x][y]+1
                    queue.append((nx,ny))
              
                    if nx==n and ny==m:
                        answer=visited[nx][ny]

bfs(0,0)
print(answer)