n, k = map(int, input().split())
prefix_sum = [0]+list(map(int, input().split()))
for i in range(1, len(prefix_sum)):
    prefix_sum[i] += prefix_sum[i-1]

result = -float('inf')
for i in range(k, n+1):
    result = max(result, prefix_sum[i]-prefix_sum[i-k])

print(result)