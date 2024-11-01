INF=1000000007
def solution(n):
    dp=[0 for _ in range(n+1)]
    dp[1]=1
    dp[2]=2
    for i in range(3,n+1):
        dp[i]=(dp[i-1]+dp[i-2])%INF
        
    return dp[n]%INF