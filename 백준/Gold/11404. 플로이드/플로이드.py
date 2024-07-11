from collections import deque

n = int(input())
m = int(input())
graph = [[float('inf') for _ in range(n+1)] for _ in range(n+1)]

for i in range(1, n+1):
    graph[i][i] = 0


for _ in range(m):
    s, e, d = map(int, input().split())
    # 같은 목적지 버스가 여러개 있을 수 있음
    graph[s][e] = min(graph[s][e], d)

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            graph[i][j] = min((graph[i][j], graph[i][k]+graph[k][j]))

for i in range(1, n+1):
    for j in range(1, n+1):
        if graph[i][j] == float('inf'):
            graph[i][j] = 0
        print(graph[i][j], end=' ')
    print()