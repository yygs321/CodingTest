n = int(input())
lst = list(input().split())


def perm(cnt):
    global n
    global max_ans
    global min_ans
    global nums

    if cnt == n+1:

        for idx, l in enumerate(lst):
            if l == '>':
                if int(nums[idx]) <= int(nums[idx+1]):
                    return
            else:
                if int(nums[idx]) >= int(nums[idx+1]):
                    return

        if int(max_ans) < int(''.join(nums)):
            max_ans = ''.join(nums)
        if int(min_ans) > int(''.join(nums)):
            min_ans = ''.join(nums)

    for i in range(10):
        if str(i) in nums:
            continue
        nums.append(str(i))
        perm(cnt+1)
        nums.pop()


nums = []
max_ans = '0'
min_ans = '10000000000'


perm(0)
print(max_ans)
print(min_ans)