k, n = map(int, input().split())
lans = []
for _ in range(k):
    lans.append(int(input()))

l = 1
r = max(lans)

ans = 0
while l <= r:
    mid = (l+r)//2

    tmp = 0
    for lan in lans:
        tmp += lan//mid

    if tmp < n:
        r = mid-1
        continue

    ans = max(ans, mid)
    l = mid+1

print(ans)