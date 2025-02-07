from collections import deque, defaultdict
import heapq

n,m=map(int,input().split())
graph=defaultdict(list)
for _ in range(m):
    a,b,c=map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

dist=[float('inf') for _ in range(n+1)]
def dijkstra(start):
    queue=[]
    heapq.heappush(queue,(0, start))
    dist[start]=0

    while queue:
        cur_d, cur= heapq.heappop(queue)

        for nxt, nxt_d in graph[cur]:
            if dist[nxt]<= cur_d+nxt_d:
                continue
            dist[nxt]=cur_d+nxt_d
            heapq.heappush(queue,(cur_d+nxt_d, nxt))

dijkstra(1)
print(dist[n])