import sys
input=sys.stdin.readline

from collections import deque

n=int(input())
size=2 # 상어의 처음 크기
map=[list(map(int,input().split())) for _ in range(n)]
queue=deque()

dx=[-1,1,0,0]
dy=[0,0,-1,1]

shark_x, shark_y=0,0

for i in range(n):
    for j in range(n):
        if map[i][j]==9:
            shark_x=i
            shark_y=j
            map[i][j]=0
          

#변경된 map을 전해줘야함
def bfs(map,r,c): #현재위치에서 먹으러갈 수 있는 물고기 중 가장 가까운 위치 반환
  ####중요: fish랑 visited를 bfs내에서 초기화해줘야한다###
  #-> 새로온 위치에서 갈수있는 fish는 매번 달라지기때문에
    fish=[]
    #0부터 거리계산에 쓰기위해서 방문하지 않은 곳은 -1로 초기화
    visited=[[-1 for _ in range(n)] for _ in range(n)]
  
    queue.append((r,c))
    visited[r][c]=0 #방문확인을 위해 처음에 1로 설정 -> 이후 계산시 -1 빼줘야함
    
    while queue:
        x,y=queue.popleft()
       
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
        
            if 0<=nx<n and 0<=ny<n:
                if visited[nx][ny]==-1 and map[nx][ny]<=size: #자기보다 작거나같은 물고기인경우 지나갈수있음
                    visited[nx][ny]=visited[x][y]+1
                    queue.append((nx,ny))
                  
                    if 1<=map[nx][ny]<size: #자기보다 작은 물고기만 먹을수 있음
                        fish.append((visited[nx][ny], nx,ny))

    
    return sorted(fish,key= lambda x: (x[0],x[1],x[2])) 
  

cnt=0
time=0
while True:
    #거리가 가까운 fish부터 방문
    result= bfs(map,shark_x, shark_y) #while문 돌면서 변경되는 map을 다시 전달해줘야함
    
    
    if len(result)==0: # 비어있으면
        print(time)
        break
  
    fdist, fx, fy =result.pop(0)
    map[fx][fy]= 0 #물고기 먹음
    time+=fdist #물고기 먹으러간 거리(시간)더해주기
    
    cnt+=1
    if cnt==size:
        size+=1
        cnt=0
  
    shark_x, shark_y=fx,fy