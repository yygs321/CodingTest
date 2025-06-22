import heapq

def solution(maps):
    answer = -1
    n=len(maps)
    m=len(maps[0])
    
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]
    
    maps=[list(m.rstrip()) for m in maps]
    visited=[[float('inf') for _ in range(m)] for _ in range(n)]
    flag=0
    lever_i,lever_j=-1,-1
    
    def find(i,j):
        nonlocal answer,n,m,flag,lever_i,lever_j
        queue=[]
        visited[i][j]=0
        heapq.heappush(queue,(0,i,j))
        
        while queue:
            d,x,y=heapq.heappop(queue)

            if d>n*m*2:
                answer=-1
                return
            
            for k in range(4):
                nx=x+dx[k]
                ny=y+dy[k]
                
                if nx<0 or ny<0 or nx>=n or ny>=m:
                    continue
                if maps[nx][ny]=='X':
                    continue
                if visited[nx][ny]<=d+1:
                    continue
                visited[nx][ny]=d+1
                if maps[nx][ny]=='L':
                    flag=1
                    lever_i,lever_j=nx,ny
                    return
                heapq.heappush(queue,(d+1,nx,ny))
                
    visited2=[[float('inf') for _ in range(m)] for _ in range(n)]        
    def go_exit(i,j):
        nonlocal answer,n,m
        queue=[]
        visited2[i][j]=visited[i][j]
        heapq.heappush(queue,(visited2[i][j],i,j))
        
        while queue:
            d,x,y=heapq.heappop(queue)
            
            if maps[x][y]=='E':
                if not flag:
                    answer=-1
                else:
                    answer=d
                return
                
            if d>n*m*2:
                answer=-1
                return
            
            for k in range(4):
                nx=x+dx[k]
                ny=y+dy[k]
                
                if nx<0 or ny<0 or nx>=n or ny>=m:
                    continue
                if maps[nx][ny]=='X':
                    continue
                if visited2[nx][ny]<=d+1:
                    continue
                
                visited2[nx][ny]=d+1
                heapq.heappush(queue,(d+1,nx,ny))
            
        
    for i in range(n):
        for j in range(m):
            if maps[i][j]=='S':
                find(i,j)
                go_exit(lever_i,lever_j)

    return answer