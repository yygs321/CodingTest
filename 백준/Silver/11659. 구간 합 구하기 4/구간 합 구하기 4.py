n, m = map(int, input().split())
prefix_sum = [0]+list(map(int, input().split()))
chapter = []
for _ in range(m):
    i, j = map(int, input().split())
    chapter.append((i, j))

for i in range(1, len(prefix_sum)):
    prefix_sum[i] += prefix_sum[i-1]

for chap in chapter:
    i, j = chap
    print(prefix_sum[j]-prefix_sum[i-1])