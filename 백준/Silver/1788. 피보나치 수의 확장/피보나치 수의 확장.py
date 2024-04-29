n = int(input())

if n == 0:
    print(0)
    print(0)
    exit()
elif n > 0:
    dp = [0 for _ in range(n+1)]
    dp[1] = 1

    for i in range(2, n+1):
        dp[i] = (dp[i-2]+dp[i-1]) % 1000000000
else:
    dp = [0 for _ in range(0, -n+1)]
    dp[1] = 1
    if n < -1:
        dp[2] = -1

    for i in range(3, -n + 1):
        if dp[i-2]-dp[i-1] >= 0:
            dp[i] = (dp[i-2]-dp[i-1]) % 1000000000
        else:
            dp[i] = (dp[i-2]-dp[i-1]) % -1000000000


if n >= 0:
    if dp[n] > 0:
        print(1)
    elif dp[n] == 0:
        print(0)
    else:
        print(-1)
    print(dp[n])
else:
    if dp[-n] > 0:
        print(1)
    elif dp[-n] == 0:
        print(0)
    else:
        print(-1)
    print(abs(dp[-n]))
