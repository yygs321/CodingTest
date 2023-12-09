cnt = 0
while True:
    n = int(input())
    if n == 0:
        break
    cnt += 1

    graph = []
    for i in range(n):
        graph.append(list(map(int, input().split())))

    dp = [[0 for _ in range(3)] for _ in range(n)]
    dp[0] = [graph[0][1], graph[0][1], min(
        graph[0][1], graph[0][1]+graph[0][2])]

    for i in range(1, n):
        dp[i][0] = min(dp[i-1][0], dp[i-1][1]) + graph[i][0]

        dp[i][1] = min(dp[i-1][0], dp[i-1][1], dp[i-1][2], dp[i][0]) + graph[i][1]

        dp[i][2] = min(dp[i-1][1], dp[i-1][2], dp[i][1]) + graph[i][2]

    print(f'{cnt}. {dp[n-1][1]}')