n = int(input())
nums = list(map(int, input().split()))

ans = 0

for x in [1, 2]:
    tmp = 0
    for num in nums:
        if tmp > 0:
            if num == x:
                tmp += 1
            else:
                tmp -= 1
        else:
            if num == x:
                tmp = 1
        ans = max(ans, tmp)

print(ans)
