def dfs(start,i, v):
    global result
    if v>=5:
      result=1
      return
      
    for gp in graph[i]:
        if visited[gp]==-1:
            visited[gp]=0
            dfs(start, gp, v+1)
            visited[gp]=-1
  

n,m=map(int,input().split())
graph=[[] for _ in range(n)]
for _ in range(m):
    a,b= map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

result=0
for i in range(n):
    visited = [-1 for _ in range(n)]
    visited[i]=0
    dfs(i,i,1)
    if result==1: break


if result==1:
    print(1)
else:
    print(0)