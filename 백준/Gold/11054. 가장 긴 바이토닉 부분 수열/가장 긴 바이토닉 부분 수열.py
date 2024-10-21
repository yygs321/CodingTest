import bisect
def lis(arr):
    if not arr:return 0
    dp = [arr[0]]

    for i in range(len(arr)):
        if dp[-1]<arr[i]:
            dp.append(arr[i])
        else:#더 작은 값으로 대체
            dp[bisect.bisect_left(dp,arr[i])] = arr[i]

    return len(dp)
 
n = int(input())
num = list(map(int,input().split()))
answer = -1
for i in range(n):
    #가운데 값은 겹치므로 하나 -1
    answer = max(answer,lis(num[:i+1])+lis([-x for x in num[i:]])-1)
print(answer)