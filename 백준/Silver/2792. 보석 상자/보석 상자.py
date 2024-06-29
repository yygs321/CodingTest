n, m = map(int, input().split())
arr = [int(input()) for _ in range(m)]

arr.sort()
left = 1
right = arr[-1]
res = 0
while left <= right:
    mid = (left + right) //2
    sum = 0

    for jewel in arr:
        cnt = jewel // mid if jewel % mid == 0 else jewel // mid + 1
        sum += cnt

    if sum > n:
        left = mid +1
    else:
        res = mid
        right = mid -1

print(res)