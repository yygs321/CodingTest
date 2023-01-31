import sys
input=sys.stdin.readline

n=int(input())
for _ in range(n):
  m=int(input())
  dp=[0]*101
  num=[1,1,1,2,2]
  for idx,n in enumerate(num):
    dp[idx+1]=n
    
  for i in range(6,m+1):
    dp[i]=(dp[i-1]+dp[i-5]) 
  
  print(dp[m])
  