import copy
def solution(triangle):
    answer = 0
    n=len(triangle)
    dp=copy.deepcopy(triangle)
    
    for i in range(1,n):
        for j in range(i+1):
            if j==0:
                dp[i][j]+=dp[i-1][0]
                continue
            elif j==i:
                dp[i][j]+=dp[i-1][j-1]
                continue
            dp[i][j]=max(dp[i-1][j-1], dp[i-1][j])+ dp[i][j]
            
    return max(dp[n-1])