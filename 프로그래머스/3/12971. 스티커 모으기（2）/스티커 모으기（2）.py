def solution(sticker):
    answer = 0
    n=len(sticker)
    sticker=[0]+sticker
    
    if n<=2:
        return max(sticker)
    
    for j in range(2):
        dp=[[-float('inf') for _ in range(2)] for _ in range(n+1)]
        dp[0][0]=0
        dp[0][1]=0
        if j==0:
            dp[1][j]=sticker[1]
        else:
            dp[1][j]=0
            
        for i in range(2,n+1):
            dp[i][0]=max(dp[i-2])+sticker[i]
            dp[i][1]=max(dp[i-1])
        
        if j==0:
            answer=max(answer,dp[n][1])
        else:
            answer=max(answer,max(dp[n]))
    
    return answer