import sys
sys.setrecursionlimit(10**6)
input=sys.stdin.readline

n=int(input())
village=[0]+list(map(int,input().split()))
graph=[[] for _ in range(n+1)]
visited=[False for _ in range(n+1)]
dp=[[0, village[i]] for i in range(n+1)] 

def dfs(start):
    visited[start]=True

    for next in graph[start]:
        if not visited[next]:
            dfs(next) #뒤에가 먼저 돌아줘야함
            dp[start][0] += max(dp[next][0], dp[next][1])
            dp[start][1] += dp[next][0]


for i in range(n-1):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

dfs(1)
print(max(dp[1][0], dp[1][1]))