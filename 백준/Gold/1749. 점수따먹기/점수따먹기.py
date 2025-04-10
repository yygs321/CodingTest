n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

# 누적합 준비
prefix_sum = [[0] * m for _ in range(n)]
for i in range(n):
    for j in range(m):
        prefix_sum[i][j] = graph[i][j]
        if i > 0:
            prefix_sum[i][j] += prefix_sum[i-1][j]

ans = -float('inf')

# 모든 (x1, x2) 행 범위 고정
for x1 in range(n):
    for x2 in range(x1, n):
        temp = [0] * m  # y 방향 압축 1D 배열 만들기
        for j in range(m):
            temp[j] = prefix_sum[x2][j]
            if x1 > 0:
                temp[j] -= prefix_sum[x1-1][j]

        # temp 배열에서 최대 연속 부분합 (카데인 알고리즘)
        current_sum = temp[0]
        max_sum = temp[0]
        for k in range(1, m):
            current_sum = max(temp[k], current_sum + temp[k])
            max_sum = max(max_sum, current_sum)
        
        ans = max(ans, max_sum)

print(ans)
