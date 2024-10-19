n,k=map(int,input().split())
num=[]
for _ in range(n):
    num.append(int(input()))

dp=[0 for _ in range(k+1)]
dp[0]=1 #num에 2가 들어있는 경우 더해줘야하므로
for i in num:
    for j in range(k+1):
        if j-i<0: continue
        dp[j]+=dp[j-i]

print(dp[k])