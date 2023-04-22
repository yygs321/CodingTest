from collections import deque

def bfs(i,j):
    global flag
    global cnt
    
    queue.append((i,j))
    visited[i][j]=flag
    
    while queue:
        x,y=queue.popleft()
    
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
      
            if nx<0 or nx>=r or ny<0 or ny>=c: continue
            if graph[nx][ny]==0 and visited[nx][ny]==0:
                visited[nx][ny]=flag
                cnt+=1
                queue.append((nx,ny))
    return

def solve(x,y):
    check=set()
    answer[x][y]+=1
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
    
        if nx<0 or nx>=r or ny<0 or ny>=c: continue
        if visited[nx][ny] not in check and graph[nx][ny]==0:
            k=visited[nx][ny]
            check.add(k)
            answer[x][y]+=lst[k]

r,c=map(int,input().split())
graph=[list(map(int,input().rstrip())) for _ in range(r)]
queue=deque()
dx=[-1,1,0,0]
dy=[0,0,-1,1]

flag=0
visited=[[0 for _ in range(c)] for _ in range(r)]
answer=[[0 for _ in range(c)] for _ in range(r)]
lst={} #그룹별 0 개수

for i in range(r):
    for j in range(c):
        if graph[i][j]==0 and visited[i][j]==0:
            cnt=1
            flag+=1
            bfs(i,j)
            lst[flag]= cnt

for i in range(r):
    for j in range(c):
        if graph[i][j]==1:
            solve(i,j)

for i in range(r):
    for j in range(c):
        print(answer[i][j]%10, end="")
    print()