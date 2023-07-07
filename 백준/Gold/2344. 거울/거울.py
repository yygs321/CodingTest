from collections import deque

def bfs(i,j,d):
    queue=deque()
    queue.append((i,j,d))

    nx,ny=0,0
    while queue:
        x,y,d=queue.popleft()
        if graph[x][y]==1:
            if d==0 or d==2:
                d+=1
            else:
                d-=1
            
        nx=x+dx[d]
        ny=y+dy[d]

        if nx<=0 or nx>n or ny<=0 or ny>m: 
            return (nx,ny)
        queue.append((nx,ny,d))

    

n,m=map(int,input().split())
graph=[[0 for _ in range(m+2)]]+[[0]+list(map(int,input().split()))+[0] for _ in range(n)]+[[0 for _ in range(m+2)]]
#동북서남
dx=[0,-1,0,1]
dy=[1,0,-1,0]


idx=0
for i in range(1,n+1):
    idx+=1
    graph[i][0]=idx
for i in range(1,m+1):
    idx+=1
    graph[n+1][i]=idx
for i in range(n,0,-1):
    idx+=1
    graph[i][m+1]=idx
for i in range(m,0,-1):
    idx+=1
    graph[0][i]=idx


result=[]

for i in range(1,n+1):
    endX, endY=bfs(i,1,0)
    result.append(graph[endX][endY])
for i in range(1,m+1):
    endX, endY=bfs(n,i,1)
    result.append(graph[endX][endY])
for i in range(n,0,-1):
    endX, endY=bfs(i,m,2)
    result.append(graph[endX][endY])
for i in range(m,0,-1):
    endX, endY=bfs(1,i,3)
    result.append(graph[endX][endY])

print(*result)