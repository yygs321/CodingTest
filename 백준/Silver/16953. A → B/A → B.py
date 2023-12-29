from collections import deque


def dfs(start, end, cnt):
    global answer
    if start >= end:
        if start != end:
            cnt = -1
        answer = min(answer, cnt)
        return

    if end % 2 == 0:
        dfs(start, end//2, cnt+1)
    if str(end)[-1] == '1':
        dfs(start, int(str(end)[:-1]), cnt+1)


start, end = map(int, input().split())

answer = int(1e9)
dfs(start, end, 1)
if answer == int(1e9):
    print(-1)
else:
    print(answer)