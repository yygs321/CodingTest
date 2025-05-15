from collections import deque

def solution(places):
    answer = []
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]
    
    def bfs(i,j,graph):
        queue=deque([(i,j)])
        visited=[[-1 for _ in range(5)] for _ in range(5)]
        visited[i][j]=0
        
        while queue:
            x,y=queue.popleft()
            
            if 0<visited[x][y] and graph[x][y]=="P":
                return False
            for k in range(4):
                nx=x+dx[k]
                ny=y+dy[k]
                
                if nx<0 or ny<0 or nx>=5 or ny>=5:
                    continue
                if visited[nx][ny]!=-1:
                    continue
                if graph[nx][ny]=="X":
                    continue
                visited[nx][ny]=visited[x][y]+1
                if visited[nx][ny]<=2:
                    queue.append((nx,ny))
        
        return True

    for place in places:
        flag=0
        for i in range(5):
            for j in range(5):
                if place[i][j]=="P":
                    if not bfs(i,j,place):
                        answer.append(0)
                        flag=1
                        break
            if flag==1:
                break
        else:
            answer.append(1)    
        
            
    
    return answer

