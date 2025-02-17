from collections import deque

def solution(storage, requests):
    n=len(storage)
    m=len(storage[0])
    answer = n*m
    
    graph=[]
    for st in storage:
        graph.append(list(st.strip()))
        
    visited=[[False for _ in range(m+2)] for _ in range(n+2)]
    for i in range(n+2):
        for j in range(m+2):
            if i==0 or j==0 or i==n+1 or j==m+1:
                visited[i][j]=True
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]
    cnt=0
    
    def crane(rq):
        nonlocal cnt
        for i in range(1,n+1):
            for j in range(1,m+1):
                if graph[i-1][j-1]==rq:
                    visited[i][j]=True
                    graph[i-1][j-1]="0"
                    cnt+=1
        
        return
    
    def container(rq):
        nonlocal cnt
        queue=deque()
        queue.append((0,0))
        tmp_visited=[[False for _ in range(m+2)] for _ in range(n+2)]
        tmp_visited[0][0]=True
        
        tmp=[]
        while queue:
            x,y=queue.popleft()
            
            for k in range(4):
                nx=x+dx[k]
                ny=y+dy[k]
                
                if nx<0 or ny<0 or nx>=n+2 or ny>=m+2:
                    continue
                if tmp_visited[nx][ny]==True:
                    continue
                
                tmp_visited[nx][ny]=True
                if visited[nx][ny]==True:
                    queue.append((nx,ny))
                else:
                    if nx<=0 or ny<=0 or nx>=n+1 or ny>=m+1:
                        continue
                    if graph[nx-1][ny-1]==rq:
                        tmp.append((nx,ny))
                        
        for i,j in tmp:
            cnt+=1
            visited[i][j]=True
            graph[i-1][j-1]="0"
            
        return
    
    for request in requests:
        if len(list(request.strip()))>1:
            crane(request[0])
        else:
            container(request[0])
                    
    return answer-cnt