from bisect import bisect_left

n = int(input())
nums = list(map(int, input().split()))

m = int(input())
existed = list(map(int, input().split()))

nums.sort()
for ex in existed:
    idx = bisect_left(nums, ex)
    if idx >= n:
        print(0)
    elif nums[idx] != ex:
        print(0)
    else:
        print(1)
