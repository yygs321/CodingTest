# n=int(input())
# rgb=[list(map(int,input().split())) for _ in range(n)]

# answer=float('inf')
# def recur(cur,price,prev):
#     global answer
#     if cur==n:
#         answer=min(answer,price)
#         return
    
#     for i in range(3):
#         if i==prev: 
#             continue
#         recur(cur+1,price+rgb[cur][i],i)

# recur(0,0,-1)
# print(answer)

n=int(input())
rgb=[list(map(int,input().split())) for _ in range(n)]

dp=[[-1]*3 for _ in range(n)]
def recur(cur,prev):
    if cur>n:
        return 746745654635
    if cur==n:
        return 0
    if dp[cur][prev]!=-1:
        return dp[cur][prev]
    
    tmp=float('inf')
    for i in range(3):
        if i==prev: 
            continue
        tmp=min(tmp, recur(cur+1,i)+rgb[cur][i])
    dp[cur][prev]=tmp

    return dp[cur][prev]

print(recur(0,-1))