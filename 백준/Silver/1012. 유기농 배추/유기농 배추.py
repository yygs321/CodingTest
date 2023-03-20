#지렁이 있으면, 이동가능
#배추가 어디어디 퍼져있는지 조사 -> 지렁이 몇마리 필요한지
from collections import deque

T= int(input())
dx=[-1,1,0,0]
dy=[0,0,-1,1]

def bfs(i,j):
    graph[i][j]=0
    queue.append((i,j))
  
    while queue:
        x,y=queue.popleft()
        
        for n in range(4):
            nx=x+dx[n]
            ny=y+dy[n]
        
            if 0<=nx<r and 0<=ny<c and graph[nx][ny]==1:
                graph[nx][ny]=0
                queue.append((nx,ny))
    

for _ in range(T):
    r,c,k= map(int,input().split())
    
    graph=[[0 for _ in range(c)] for _ in range(r)]
    queue=deque()
    count=0
    
    for i in range(k):
        x,y=map(int,input().split())
        graph[x][y]=1
  
    for j in range(r):
        for l in range(c):
            if graph[j][l]==1:
                count+=1
                bfs(j,l)
  
    print(count)