from collections import deque,defaultdict

n=int(input())
parents=[i for i in range(n+1)]
graph=defaultdict(list)
for _ in range(n-1):
    a,b=map(int,input().split())

    graph[a].append(b)
    graph[b].append(a)

def bfs():
    queue=deque([1])
    visited=[False for _ in range(n+1)]
    visited[1]=True

    while queue:
        cur=queue.popleft()
        for nxt in graph[cur]:
            if visited[nxt]:
                continue
            visited[nxt]=True
            parents[nxt]=cur
            queue.append(nxt)

bfs()
for i in range(2,n+1):
    print(parents[i])



