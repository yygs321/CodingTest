from collections import deque, defaultdict
import heapq

v, e = map(int, input().split())
point = int(input())
graph = defaultdict(list)

for _ in range(e):
    start, end, val = map(int, input().split())
    graph[start].append((end, val))

dist = [float('inf') for _ in range(v+1)]


def dijkstra(start):
    queue = []
    heapq.heappush(queue, (0, start))
    dist[start] = 0

    while queue:
        cur_dist, cur = heapq.heappop(queue)

        for nxt, val in graph[cur]:
            if dist[nxt] <= dist[cur]+val:
                continue
            dist[nxt] = dist[cur]+val
            heapq.heappush(queue, (dist[nxt], nxt))

dijkstra(point)
for d in dist[1:]:
    if d == float('inf'):
        print("INF")
    else:
        print(d)
