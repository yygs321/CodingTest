def solution(money):
    answer = 0
    n=len(money)
    money=[0]+money
    dp=[[0]*2 for _ in range(n+1)]
    # 첫번째 집 선택하는 경우
    for i in range(1,n+1):
        dp[i][0]=max(dp[i-1])
        dp[i][1]=max(dp[i-1][1], dp[i-1][0]+money[i])
    a=dp[n][0] #마지막 집 선택 X
    
    
    #첫번째집 선택 안하는 경우
    dp2=[[0]*2 for _ in range(n+1)]
    for i in range(2,n+1):
        dp2[i][0]=max(dp2[i-1])
        dp2[i][1]=max(dp2[i-1][1], dp2[i-1][0]+money[i])
    b=max(dp2[n])
    
    return max(a,b)