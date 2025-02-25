INF=1000000007
def solution(m, n, puddles):
    puddles_set={(py,px) for px,py in puddles}
    answer = 0
    
    dp=[[0]*(m+1) for _ in range(n+1)]
    dp[1][1]=1
    
    for i in range(1,n+1):
        for j in range(1,m+1):
            if i==1 and j==1: continue
            
            if (i,j) in puddles_set:
                dp[i][j]=0
                continue 
                
            dp[i][j]=(dp[i-1][j]+dp[i][j-1])%INF
            
    return (dp[n][m])%INF