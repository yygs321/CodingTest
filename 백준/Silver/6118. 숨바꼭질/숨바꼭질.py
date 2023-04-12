from collections import deque

def bfs():
  queue.append(1)
  visited[1]=0

  while queue:
    x=queue.popleft()
    for gp in graph[x]:
      if visited[gp]==-1:
        queue.append(gp)
        visited[gp]=visited[x]+1
    


n,m=map(int,input().split())
# 1번 헛간부터
graph=[[] for _ in range(n+1)]
for i in range(m):
    a,b=map(int,input().split())

    graph[a].append(b)
    graph[b].append(a)



visited=[-1 for i in range(n+1)]
visited[1]=0

queue=deque()
bfs()

maxIdx= visited.index(max(visited))
print(maxIdx, visited[maxIdx], visited.count(visited[maxIdx]))