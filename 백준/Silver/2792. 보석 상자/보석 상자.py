import math
n, m = map(int, input().split())
jewely = []
for _ in range(m):
    jewely.append(int(input()))

l, r = 1, max(jewely)
result = r
while l <= r:
    mid = (l+r)//2
    tmp = 0

    for j in jewely:
        tmp += math.ceil(j/mid)  # 나머지가 얼마든 1명으로 계산
    if tmp > n:
        l = mid+1
        continue

    result = min(result, mid)
    r = mid-1

print(result)