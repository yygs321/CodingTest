import sys
sys.setrecursionlimit(10**6)

n = int(input())
graph = [[] for _ in range(n)]
for i in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)

nums = list(map(int, input().split()))
visited = [False for _ in range(n)]


def dfs(cur):
    if not graph[cur]:
        visited[cur] = True
        return max(0, nums[cur])

    tmp = nums[cur]
    for nxt in graph[cur]:
        if not visited[nxt]:
            val = dfs(nxt)
            if val <= 0:
                continue
            tmp += val

    visited[cur] = True
    return tmp


print(dfs(0))
