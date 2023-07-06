from collections import deque

n,m=map(int,input().split())
graph=[list(map(int,input().split())) for _ in range(n)]
dx=[-1,1,0,0]
dy=[0,0,-1,1]
ice=[[0 for _ in range(m)] for _ in range(n)]
answer=0
#1. 빙하 각각 주변 0 개수 세기
#2. 그래프에서 개수만큼 높이 빼기
# 1,2 반복하는데 1에서 주변 0개수가 4인게 2개 이상이 나오면 break
# 만약 전부다 녹으면 0


def count(graph,i,j):
    global total_ice
    cnt=0
    for k in range(4):
        nx=i+dx[k]
        ny=j+dy[k]

        if graph[nx][ny]==0:
            cnt+=1
    
    ice[i][j]=cnt

def melt(graph):
    for i in range(n):
        for j in range(m):
            tmp=graph[i][j]- ice[i][j]
            if tmp<0:
                graph[i][j]=0
            else:
                graph[i][j]=tmp

def group(i,j):
    queue=deque()

    queue.append((i,j))
    visited[i][j]=1

    while queue:
        x,y=queue.popleft()
        for k in range(4):
            nx=x+dx[k]
            ny=y+dy[k]

            if nx<0 or nx>=n or ny<0 or ny>=m: continue
            if visited[nx][ny]==1: continue
            if graph[nx][ny]!=0:
                visited[nx][ny]=1
                queue.append((nx,ny))

while True:
    total_ice=0
    visited=[[0 for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if graph[i][j]==0: continue
            count(graph, i,j)

    melt(graph)
    cnt=0
    for i in range(n):
        for j in range(m):
            if graph[i][j]==0: continue
            if visited[i][j]==1: continue
            cnt+=1
            if cnt>1: break
            group(i,j)
    
    answer+=1

    tmp_sum=0
    for k in range(n):
        tmp_sum+=sum(graph[k])

    if cnt==1: continue
    else:
        if tmp_sum==0:
            print(0)
        else:
            print(answer)
        break
