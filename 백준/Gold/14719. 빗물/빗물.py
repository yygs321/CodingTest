r,c = map(int, input().split())
lst = list(map(int, input().split()))

ans = 0
for i in range(1, c - 1):
    #각 위치에서 양 옆으로 가장 큰 값들 중
    left = max(lst[:i])
    right = max(lst[i+1:])

    #둘 중 작은 값의 높이까지만 빗물이 찬다
    min_value = min(left, right)

    if lst[i] < min_value:
        ans += min_value - lst[i]

print(ans)