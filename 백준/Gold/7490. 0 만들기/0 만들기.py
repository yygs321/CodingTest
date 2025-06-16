test = int(input())
for t in range(test):
    answer = []
    n = int(input())
    nums = [i for i in range(1, n+1)]

    flags = ["+", "-", " "]

    def dfs(cur, cnt):
        global n

        cur.append(str(nums[cnt]))
        if cnt == n-1:
            tmp = "".join(cur)
            tmp2 = tmp.replace(" ", "")
            if eval(tmp2) == 0:
                answer.append(tmp)
            return

        for flag in flags:
            dfs(cur+[flag], cnt+1)

    dfs([], 0)

    answer.sort()
    for ans in answer:
        print(ans)

    if t != test-1:
        print()
