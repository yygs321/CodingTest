# 1~k번
#s초 후 x,y에 들어있는 바이러스 종류 출력
#번호 낮은것부터 먼저 증식
# 없으면 0
from collections import deque

def bfs():
    global s
    while queue:
        
        virus,x1,y1=queue.popleft()
        if visited[x1][y1]>=s: #s초 까지만 진행
            return
          
        for i in range(4):
            nx=x1+dx[i]
            ny=y1+dy[i]
            if 0<=nx<n and 0<=ny<n:
                #원래 바이러스 있는 곳
                if graph[nx][ny]!=0 and visited[nx][ny]==0: continue
                  
                if graph[nx][ny]==0:
                    if visited[nx][ny]==0: #처음 방문하는 경우
                        graph[nx][ny]=virus
                        visited[nx][ny]=visited[x1][y1]+1
                else:
                    if visited[nx][ny]<visited[x1][y1]+1: continue
                    elif visited[nx][ny]>visited[x1][y1]+1:
                        graph[nx][ny]=virus
                        visited[nx][ny]=visited[x1][y1]+1
                    else: #같으면 더 작은 값
                        graph[nx][ny]=min(graph[nx][ny], virus)
                      
                queue.append((graph[nx][ny],nx,ny))


n,k= map(int,input().split())
graph=[]
dx=[-1,1,0,0]
dy=[0,0,-1,1]
visited=[[0 for _ in range(n)] for _ in range(n)]
for _ in range(n):
    graph.append(list(map(int,input().split())))

s,x,y=map(int,input().split())
queue=deque()
for i in range(n):
    for j in range(n):
        if graph[i][j]==0:continue
        queue.append((graph[i][j],i,j))

bfs()

print(graph[x-1][y-1])