import sys
sys.setrecursionlimit(10**6)

def dfs(i):
    for gp in graph[i]:
        c,v=gp
        if visited[c]==-1:
            visited[c]=visited[i]+v
            dfs(c)
  
n=int(input())
graph=[[] for _ in range(n+1)]
for _ in range(n-1):
    p,c,v=map(int,input().split())
    graph[p].append([c,v])
    graph[c].append([p,v])

visited=[-1 for _ in range(n+1)]
visited[1]=0

dfs(1)

maxIdx=visited.index(max(visited))
visited=[-1 for _ in range(n+1)]
visited[maxIdx]=0

dfs(maxIdx)

print(max(visited))