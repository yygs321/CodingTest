# n,k=map(int,input().split())
# stucks=[list(map(int,input().split())) for _ in range(n)]

# ans=0
# def recur(cur, total_w, total_v):
#     global ans
#     if total_w>k:
#         return
#     if cur==n:
#         ans=max(ans,total_v)

#     for i in range(cur,n):
#         recur(cur+1, total_w+stucks[i][0], total_v+stucks[i][1])
#         recur(cur+1, total_w, total_v)
    
# recur(0,0,0)
# print(ans)

n,k=map(int,input().split())
stucks=[list(map(int,input().split())) for _ in range(n)]

dp=[[-1]*(k+1) for _ in range(n)]
def recur(cur, total_w):
    if total_w>k:
        return -43534852352
    if cur==n:
        return 0
    if dp[cur][total_w]!=-1:
        return dp[cur][total_w]

    dp[cur][total_w]=max(recur(cur+1, total_w+stucks[cur][0])+stucks[cur][1], recur(cur+1, total_w))

    return dp[cur][total_w]
    
print(recur(0,0))