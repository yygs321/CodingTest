from collections import deque

#S: 양, W: 늑대
#늑대 막을 수 있으면 1 출력
# 울타리 D 설치한 목장 상태 출력
R,C= map(int,input().split())
graph=[list(input().rstrip()) for _ in range(R)]
dx=[-1,1,0,0]
dy=[0,0,-1,1]
queue=deque()

for i in range(R):
    for j in range(C):
        if graph[i][j]=='W':
            queue.append((i,j))

result=1
def bfs():
    while queue:
        x,y= queue.popleft()
      
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
        
            if 0<=nx<R and 0<=ny<C:
                if graph[nx][ny]=='S': #양이 바로 붙어있으면 
                    result=0
                    print(result)
                    exit()
          
                if graph[nx][ny]=='.':
                    graph[nx][ny]='D'

bfs()
print(result)
for i in range(R):
    for j in range(C):
        print(graph[i][j], end="")
    print()