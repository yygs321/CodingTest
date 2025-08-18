def solution(n, money):
    INF=1000000007
    
    dp=[0 for _ in range(n+1)]
    dp[0]=1
    
    for m in money: # 중복 방지하려면 한 화폐로 만들 수 있는 수 한 번씩만 체크
        for i in range(m,n+1):
            dp[i]=(dp[i]+dp[i-m])%INF

    return dp[n]