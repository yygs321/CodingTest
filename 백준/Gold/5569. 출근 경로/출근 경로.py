# w,h=map(int,input().split())

# cnt=0
# #동, 북
# dx=[0,1]
# dy=[1,0]
# def recur(i,j, prev_dir, changed):
#     global cnt
#     if i==h-1 and j==w-1:
#         cnt+=1
#         return
    
#     for k in range(2):
#         if changed==1 and prev_dir!=k:
#             continue
#         nx=i+dx[k]
#         ny=j+dy[k]

#         if nx<0 or ny<0 or nx>=h or ny>=w:
#             continue
#         if prev_dir==-1 or prev_dir==k:
#             recur(nx,ny,k,0)
#         else:
#             recur(nx,ny,k,1)

# recur(0,0,-1,0)
# print(cnt)

MOD=100000
w,h=map(int,input().split())


#동, 북
dx=[0,1]
dy=[1,0]

dp= [[[[ -1 for _ in range(2)] for _ in range(2)] for _ in range(w)] for _ in range(h)]

def recur(i,j, prev_dir, changed):
    if i==h-1 and j==w-1:
        return 1
    if dp[i][j][prev_dir][changed]!=-1:
        return dp[i][j][prev_dir][changed]
    
    ret=0
    for k in range(2):
        if changed==1 and prev_dir!=k:
            continue
        nx=i+dx[k]
        ny=j+dy[k]

        if nx<0 or ny<0 or nx>=h or ny>=w:
            continue
        if prev_dir==-1 or prev_dir==k:
            ret+= recur(nx,ny,k,0)
        else:
            ret+= recur(nx,ny,k,1)
    
    ret%=MOD
    dp[i][j][prev_dir][changed]=ret
    return dp[i][j][prev_dir][changed]

print(recur(0,0,-1,0))