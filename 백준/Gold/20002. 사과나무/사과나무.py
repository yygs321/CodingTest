n = int(input())
graph = [[0]+list(map(int, input().split())) for _ in range(n)]
graph = [[0 for _ in range(n+1)]]+graph

answer = -float('inf')
prefix_sum = [[0 for _ in range(n+1)] for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, n+1):
        prefix_sum[i][j] = prefix_sum[i][j-1] + \
            prefix_sum[i-1][j]-prefix_sum[i-1][j-1]+graph[i][j]

for k in range(1, n+1):
    for i in range(k, n+1):
        for j in range(k, n+1):
            tmp = prefix_sum[i][j]-prefix_sum[i][j-k] - \
                prefix_sum[i-k][j]+prefix_sum[i-k][j-k]
            answer = max(answer, tmp)

print(answer)
