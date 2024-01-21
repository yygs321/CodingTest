from collections import deque
def solution(land):
    n=len(land)
    m=len(land[0])
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]
    result={}
    

    def bfs(i,j,num):
        queue=deque()
        queue.append((i,j))
        land[i][j]=num
        cnt=1
        
        while queue:
            x,y=queue.popleft()
            
            for k in range(4):
                nx=x+dx[k]
                ny=y+dy[k]
                if nx<0 or ny<0 or nx>=n or ny>=m: continue
                if land[nx][ny]==1: 
                    land[nx][ny]=num
                    queue.append((nx,ny))
                    cnt+=1
        result[num]=cnt
                
    num=1
    for i in range(n):
        for j in range(m):
            if land[i][j]==1:
                num+=1
                bfs(i,j,num)
    
    answer=0
    for i in range(m):
        answer_set=set()
        tmp=0
        for j in range(n):
            if land[j][i]==0:
                continue
            answer_set.add(land[j][i])
    
        for a in list(answer_set):
            tmp+=result[a]
        answer=max(answer, tmp)
        
    return answer