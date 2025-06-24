from collections import deque

def solution(arr):
    n=len(arr)
    answer = [0,0]
    
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]
    completed=[[False for _ in range(n)] for _ in range(n)]    
    prefix_sum=[[0 for _ in range(n+1)] for _ in range(n+1)]

    def check(i,j, dist):
        for x in range(i, i + dist):
            for y in range(j, j + dist):
                completed[x][y] = True
    
    for i in range(1,n+1):
        for j in range(1,n+1):
            prefix_sum[i][j]=prefix_sum[i-1][j]+prefix_sum[i][j-1]-prefix_sum[i-1][j-1]+arr[i-1][j-1]
    
    m=n
    while m >=1:
        for i in range(n,0,-m):
            for j in range(n,0,-m):
                if completed[i-1][j-1]:
                    continue
                tmp=prefix_sum[i][j]-prefix_sum[i-m][j]-prefix_sum[i][j-m]+prefix_sum[i-m][j-m]
                
                if tmp==0 or tmp==m**2:
                    answer[arr[i-1][j-1]]+=1
                    check(i-m,j-m,m)
        m//=2
    
    return answer