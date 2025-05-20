A = input().rstrip()
B = input().rstrip()
n = len(A)
m = len(B)

dp = [[0] * (m + 1) for _ in range(n + 1)]

#dp[i][j]= A의 i번째 문자까지와 B의 j번째 문자까지를 비교했을 때 LCS의 길이
for i in range(1, n + 1):
    for j in range(1, m + 1):
        if A[i - 1] == B[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

print(dp[n][m])
