# n=int(input())

# days=[[0,0] for _ in range(n+1)]
# for i in range(1,n+1):
#     t,p=map(int,input().split())
#     days[i]=[t,p]

# answer=0
# def dfs(start, price):
#     global answer
#     if start>n+1:
#         return
#     if start==n+1:
#         answer=max(answer,price)
#         return
    
#     dfs(start+days[start][0], price+days[start][1])
#     dfs(start+1,price)

# dfs(1,0)
# print(answer)
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

n=int(input())

days=[[0,0]]+[list(map(int,input().split())) for _ in range(n)]

dp=[-1]*(n+1)
def dfs(start):
    if start>n+1:
        return -float('inf')
    if start==n+1:
        return 0
    if dp[start]!=-1:
        return dp[start]
    
    dp[start]= max(dfs(start+days[start][0])+days[start][1],dfs(start+1))
    return dp[start]
    
print(dfs(1))