def solution(info, n, m):
    l = len(info)
    answer = float('inf')
    visited = set()

    def dfs(cur, a, b):
        nonlocal answer

        if cur == l:
            if a < n and b < m:
                answer = min(answer, a)
            return

        key = (cur, a, b)
        if key in visited:
            return
        visited.add(key)

        if a + info[cur][0] < n:
            dfs(cur + 1, a + info[cur][0], b)

        if b + info[cur][1] < m:
            dfs(cur + 1, a, b + info[cur][1])

    dfs(0, 0, 0)

    return -1 if answer == float('inf') else answer
