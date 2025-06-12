n = int(input())
nums = list(map(int, input().split()))

l, r = 0, n - 1
answer = 0

while l < r:
    answer = max(answer, (r-l-1) * min(nums[l], nums[r]))

    if nums[l] < nums[r]:
        l += 1
    else:
        r -= 1

print(answer)
