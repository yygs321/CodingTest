from collections import deque

t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    d = [0]+list(map(int, input().split()))
    graph = [[] for _ in range(n + 1)]
    indegree = [0 for _ in range(n + 1)]
    dp = [0 for _ in range(n + 1)]

    for i in range(k):
        a, b = map(int, input().split())
        graph[a].append(b)
        indegree[b] += 1

    w = int(input())

    queue = deque()
    for i in range(1, n + 1):
        if indegree[i] == 0:
            queue.append(i)
            dp[i] = d[i]

    while queue:
        x = queue.popleft()

        for i in graph[x]:
            indegree[i] -= 1
            dp[i] = max(dp[i], dp[x] + d[i])
            if indegree[i] == 0:
                queue.append(i)

    print(dp[w])