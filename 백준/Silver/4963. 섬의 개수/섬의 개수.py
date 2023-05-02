from collections import deque
queue=deque()
dx=[-1,1,0,0,-1,1,-1,1]
dy=[0,0,-1,1,1,-1,-1,1]

def bfs(i,j):
    global cnt
    graph[i][j]=cnt
    queue.append((i,j))
  
    while queue:
        x,y=queue.popleft()
        for k in range(8):
            nx=x+dx[k]
            ny=y+dy[k]
      
            if nx<0 or nx>=r or ny<0 or ny>=c: continue
            if graph[nx][ny]==1:
                graph[nx][ny]=cnt
                queue.append((nx,ny))
      

c,r=map(int,input().split())
result=[]
while c!=0 and r!=0:
    graph=[list(map(int,input().split())) for _ in range(r)]

    cnt=1
    for i in range(r):
        for j in range(c):
            if graph[i][j]==1:
                cnt+=1
                bfs(i,j)
    
    result.append(cnt-1)

    c,r=map(int,input().split())

print(*result, sep="\n")