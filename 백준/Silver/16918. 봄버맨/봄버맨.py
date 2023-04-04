from collections import deque

def zero():
    global cnt
    for i in range(r):
        for j in range(c):
            if graph[i][j]!='O':
                visited[i][j]=cnt
                graph[i][j]='O'
        
def bfs():
    global cnt
  
    while queue:
        x,y=queue.popleft()
        visited[x][y]=cnt
        
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
        
            if 0<=nx<r and 0<=ny<c and graph[nx][ny]=='.':
                visited[nx][ny]=visited[x][y]
                graph[nx][ny]='O'
      
    cnt+=1
    zero()


def bomb():
    global cnt
    for i in range(r):
        for j in range(c):
            if visited[i][j]==cnt-2:
                graph[i][j]='.'
    

r,c,n=map(int,input().split())
graph=[]
visited=[[0 for _ in range(c)] for _ in range(r)]
dx=[-1,1,0,0]
dy=[0,0,-1,1]

for i in range(r):
    graph.append(list(input().rstrip()))

queue=deque()

cnt=1
while cnt<n:
    for i in range(r):
        for j in range(c):
            if graph[i][j]=='O':
                queue.append((i,j))
      
    bfs()
    if cnt==n:
        break
  
    cnt+=1
    bomb()
  
for i in range(r):
    for j in range(c):
        print(graph[i][j], end="")
    print()