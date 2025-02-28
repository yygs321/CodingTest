n=int(input())
trains=[0]+list(map(int,input().split()))
k=int(input())
for i in range(1,n+1):
    trains[i]+=trains[i-1]
dp=[[0 for _ in range(n+1)] for _ in range(4)]

for i in range(1,4):
    for j in range(k,n+1):
        dp[i][j]=max(dp[i][j-1],dp[i-1][j-k]+(trains[j]-trains[j-k]))

print(dp[3][n])