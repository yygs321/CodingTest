n, s = map(int, input().split())
nums = list(map(int, input().split()))
nums_set = ()

ans = 0


def comb(start, cnt, tmp):
    global ans
    if cnt >= 1:
        if tmp in nums_set:
            return
        if sum(tmp) == s:
            ans += 1
        if cnt == n:
            return

    for i in range(start, n):
        tmp.append(nums[i])
        comb(i+1, cnt+1, tmp)
        tmp.pop()


comb(0, 0, [])
print(ans)