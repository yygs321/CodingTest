import heapq
n, m, x = map(int, input().split())
graph = [[] for _ in range(n + 1)]
ans = [0 for _ in range(n)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((c, b))


def dijk(start):
    q = []
    heapq.heappush(q, (0, start))
    dist = [int(1e9) for _ in range(n + 1)]
    dist[start] = 0

    while q:
        cost, now = heapq.heappop(q)

        for d, next in graph[now]:
            if dist[next] > cost + d:
                dist[next] = cost + d
                heapq.heappush(q, (cost + d, next))

    return dist


r = -1
for i in range(1, n + 1):
    if i != x:
        go = dijk(i)[x]
        goal = dijk(x)[i]
        r = max(r, go + goal)

print(r)