from collections import deque
n=int(input())
dx=[-1,1,0,0]
dy=[0,0,-1,1]
cnt=0

def bfs(i,j):
    queue.append((i,j))
    lst[i][j]=graph[i][j]
  
    while queue:
        x,y=queue.popleft()
        for i in range(4):
            nx= x+ dx[i]
            ny= y+ dy[i]
            if 0<=nx<n and 0<=ny<n:
                if lst[x][y]+graph[nx][ny]<lst[nx][ny]:
                    lst[nx][ny]=lst[x][y]+graph[nx][ny]
                    queue.append((nx,ny))

while n:
    cnt+=1
    graph=[]
    lst=[[int(1e9) for _ in range(n)] for _ in range(n)]
    queue=deque()
    for _ in range(n):
        graph.append(list(map(int,input().split())))
  
    bfs(0,0)
    result=lst[n-1][n-1]
  
    print(f'Problem {cnt}: {result}')
    n=int(input())