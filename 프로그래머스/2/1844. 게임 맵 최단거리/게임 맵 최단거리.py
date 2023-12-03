from collections import deque
INF=int(1e9)

def bfs(maps, i,j,n,m,visited):   
    queue=deque()
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]
    
    queue.append((i,j))
    visited[i][j]=1
    
    while queue:
        x,y=queue.popleft()
        for k in range(4):
            nx=x+dx[k]
            ny=y+dy[k]
            
            if nx<0 or ny<0 or nx>=n or ny>=m: continue
            if visited[nx][ny]!=INF: continue
            if maps[nx][ny]==0: continue
            visited[nx][ny]=min(visited[nx][ny],visited[x][y]+1)
            queue.append((nx,ny))
        

def solution(maps):
    n=len(maps)
    m=len(maps[0])
    visited=[[INF for _ in range(m)] for _ in range(n)]

    
    bfs(maps,0,0,n,m,visited)
    
    if visited[n-1][m-1]==INF:
        return -1
    return visited[n-1][m-1]