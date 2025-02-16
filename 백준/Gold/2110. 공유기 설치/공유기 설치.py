n, c = map(int, input().split())
house = sorted(list(int(input()) for _ in range(n)))

# 공유기 사이 거리
l = 1
r = house[-1]-house[0]
result = 1

while l <= r:
    # 일단 설정한 공유기 사이의 최소 거리
    mid = (l+r)//2
    last = house[0]
    cnt = 1

    for i in range(1, n):
        if house[i] >= last+mid:
            cnt += 1
            last = house[i]

    if cnt < c: 
        # 설치된 공유기 수가 적으면 최소거리가 너무 컸던 것
        r = mid-1
    else:
        result=max(result, mid)
        l = mid+1

print(result)
