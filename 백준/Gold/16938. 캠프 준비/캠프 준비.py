n, l, r, x = map(int, input().split())
problems = list(map(int, input().split()))
problems.sort()
ans = 0


def comb(start, cnt, tmp):
    global ans
    if cnt >= 2:
        if (l <= sum(tmp) <= r) and (max(tmp)-min(tmp) >= x):
            ans += 1

        if cnt == n:
            return

    for i in range(start, n):
        tmp.append(problems[i])
        comb(i+1, cnt+1, tmp)
        tmp.pop()


comb(0, 0, [])
print(ans)