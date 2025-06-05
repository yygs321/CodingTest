from bisect import bisect_left

n = int(input())
nums = [0]+list(int(input()) for _ in range(n))

prefix_sum = [0 for _ in range(2*n+1)]
for i in range(1, n+1):
    prefix_sum[i] = prefix_sum[i-1]+nums[i % (n+1)]
for i in range(n+1, 2*n+1):
    if i % n == 0:
        prefix_sum[i] = prefix_sum[i-1]+nums[(i+1) % (n+1)]
        continue
    prefix_sum[i] = prefix_sum[i-1]+nums[i % n]

answer = 0
for i in range(1, n+1):
    tmp = prefix_sum[i:n+i+1]
    mid = (tmp[0]+tmp[-1])//2
    idx = bisect_left(tmp, mid)

    x = tmp[idx]-tmp[0]
    y = tmp[-1]-tmp[idx]

    a = tmp[idx-1]-tmp[0]
    b = tmp[-1]-tmp[idx-1]

    if abs(x-y) < abs(a-b):
        answer = max(answer, min(x, y))
    else:
        answer = max(answer, min(a, b))

print(answer)
