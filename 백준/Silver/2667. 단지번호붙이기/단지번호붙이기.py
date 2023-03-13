from collections import deque
n=int(input())
#띄어쓰기없는 배열 받아올땐 rstrip
map=[list(map(int,input().rstrip())) for _ in range(n)]
dx=[-1,1,0,0]
dy=[0,0,-1,1]
visited=[[False for _ in range(n)] for _ in range(n)]
queue=deque()
result=[]

def bfs(r,c):
    global result
    cnt=1
    queue.append((r,c))
    visited[r][c]=True
  
    while queue:
        x,y=queue.pop()
    
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<n:
                if map[nx][ny]==1 and visited[nx][ny]==False:
                    visited[nx][ny]=True
                    cnt+=1
                    queue.append((nx,ny))
    result.append(cnt)

for i in range(n):
    for j in range(n):
        if map[i][j]==1 and visited[i][j]==False:
            bfs(i,j)

result.sort()
print(len(result))
for r in result:
    print(r)