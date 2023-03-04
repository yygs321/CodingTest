from collections import deque

#열 m, 행 n
m, n = map(int, input().split())
lst=[list(map(int,input().split())) for _ in range(n)]
queue=deque([])
dx=[-1,1,0,0]
dy=[0,0,-1,1]
answer=0

for i in range(n):
    for j in range(m):
        if lst[i][j]==1: #익은 토마토가 나오면
            queue.append([i,j,0])

while queue:
    r,c,day=queue.popleft()
  
    for i in range(4):
        nx=r+dx[i]
        ny=c+dy[i]
    
        if 0 <= nx < n and 0 <= ny < m and ny<m and lst[nx][ny]==0:
            answer=day+1
            lst[nx][ny]=1
            queue.append([nx,ny,day+1])

for i in range(n):
    for j in range(m):
        if lst[i][j]==0:
            print(-1)
            exit(0)

print(answer)