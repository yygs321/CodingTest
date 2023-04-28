#바라보는 방향이 있음
#현재칸 청소
# 4방탐색 
  #=> 빈칸이 없으면 
    # 바라보는 방향 유지한채 한칸 후진
    # 후진칸이 벽이면 작동 멈춤
  #=> 빈칸 있으면 
    # 반시계방향 90도 북, 서, 남, 동
    # 바라보는 방향 앞쪽 칸이 빈칸이면 한칸 전진하고 청소
from collections import deque

def bfs(i,j,v):
    global result
    queue.append((i,j,v))
  
  
    while queue:
        x,y,d=queue.popleft()
        if graph[x][y]==0:
            graph[x][y]=2
            result+=1
        
        for i in range(3,-1,-1):
            nx=x+dx[(d+i)%4]
            ny=y+dy[(d+i)%4]
      
            if nx<0 or nx>=n or ny<0 or ny>=m: continue
            if graph[nx][ny]!=0: continue
    
            queue.append((nx,ny,(d+i)%4)) 
            break
    
        else: #청소안된 칸이 없으면
            nx=x+dx[(d+2)%4]
            ny=y+dy[(d+2)%4]
            #후진 불가
            if nx<0 or nx>=n or ny<0 or ny>=m: return
            if graph[nx][ny]==1: continue
            #벽만 아니면 후진 가능
            queue.append((nx,ny,d)) #방향 유지한채로 후진
        

n,m=map(int,input().split())
r,c,d=map(int,input().split())


graph=[list(map(int,input().split())) for _ in range(n)]
#d=0,1,2,3 북동남서
dx=[-1,0,1,0]
dy=[0,1,0,-1]
queue=deque()
result=0

bfs(r,c,d)
print(result)