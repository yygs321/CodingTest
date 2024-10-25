from collections import deque
n=int(input())
graph=[list(map(int,input().rstrip())) for _ in range(n)]
ans=[]
dx=[-1,1,0,0]
dy=[0,0,-1,1]
visited=[[False]*n for _ in range(n)]

def bfs(i,j):
    queue=deque()
    queue.append((i,j))
    visited[i][j]=True
    cnt=1

    while queue:
        x,y=queue.popleft()

        for k in range(4):
            nx=x+dx[k]
            ny=y+dy[k]

            if nx<0 or ny<0 or nx>=n or ny>=n:
                continue
            if visited[nx][ny]==True:
                continue
            if graph[nx][ny]==0:
                continue
            visited[nx][ny]=True
            cnt+=1
            queue.append((nx,ny))
    return cnt



for i in range(n):
    for j in range(n):
        if graph[i][j]==0:
            continue
        if visited[i][j]==True:
            continue
        cnt=bfs(i,j)
        ans.append(cnt)

print(len(ans))
for a in sorted(ans):
    print(a)