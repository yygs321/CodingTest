n, c = map(int, input().split())
house = sorted(list(int(input()) for _ in range(n)))

# 공유기 사이 거리 (1이 최소)
l = 1
r = house[-1]-house[0]
result = 1

while l <= r:
    mid = (l+r)//2
    last = house[0]
    cnt = 1  # 처음 하나는 무조건 설치

    for i in range(1, n):
        if house[i] >= last+mid:
            cnt += 1
            last = house[i]

    if cnt >= c:
        result=max(result, mid)
        l = mid+1
    else:
        r = mid-1

print(result)