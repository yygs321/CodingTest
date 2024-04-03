# 정글, 바다, 얼음
n, m = map(int, input().split())
k = int(input())
graph = [[0 for _ in range(m+1)]]
graph += [[0]+list(input().rstrip()) for _ in range(n)]
result = [[] for _ in range(n)]

result = [[[0, 0, 0] for _ in range(m+1)] for _ in range(n+1)]
for i in range(1, n+1):
    for j in range(1, m+1):
        if graph[i][j] == 'J':
            result[i][j][0] += 1
        elif graph[i][j] == 'O':
            result[i][j][1] += 1
        elif graph[i][j] == 'I':
            result[i][j][2] += 1
        result[i][j][0] = result[i][j-1][0] + result[i-1][j][0] - result[i-1][j-1][0] +result[i][j][0]
        result[i][j][1] = result[i][j-1][1] + result[i-1][j][1] - result[i-1][j-1][1] +result[i][j][1]
        result[i][j][2] = result[i][j-1][2] + result[i-1][j][2] - result[i-1][j-1][2] +result[i][j][2]


answer = []
for i in range(k):
    sx, sy, ex, ey = map(int, input().split())
    tmp = []
    for j in range(3):
        tmp.append(result[ex][ey][j]-result[ex][sy-1][j] - result[sx-1][ey][j]+result[sx-1][sy-1][j])
    answer.append(tmp)


for i in range(k):
    print(*answer[i])