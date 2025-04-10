import sys
sys.setrecursionlimit(10**6)


def solution(maps):
    answer = []
    graph=[]
    for map in maps:
        graph.append(list(map))
    
    n=len(graph)
    m=len(graph[0])
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]
    
    def dfs(i,j):
        tmp=int(graph[i][j])
        
        for k in range(4):
            nx=i+dx[k]
            ny=j+dy[k]

            if nx<0 or ny<0 or nx>=n or ny>=m:
                continue
            if visited[nx][ny]:
                continue
            if graph[nx][ny]=='X':
                continue
                
            visited[nx][ny]=True
            tmp+=dfs(nx,ny)
        
        return tmp
        
    visited=[[False for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if graph[i][j]=='X':
                continue
            if visited[i][j]:
                continue
            visited[i][j]=True
            answer.append(dfs(i,j))
    
    return list(sorted(answer)) if answer else [-1]