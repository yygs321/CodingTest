from collections import deque


def bf(start):
    tmp = [10001 for _ in range(n+1)]
    tmp[start] = 0
    for i in range(1, n+1):
        for s in range(1, n+1):
            for e, t in graph[s]:
                if tmp[e] > tmp[s] + t:
                    tmp[e] = tmp[s] + t
                    if e == s and tmp[e] < 0:
                        return True
                    if i == n:  # n번 이후에도 값이 갱신되면 음수 사이클 존재.
                        return True
    return False


T = int(input())
for tc in range(T):
    n, m, w = map(int, input().split())
    graph = [[] for _ in range(n+1)]

    # 도로는 방향이 X
    for i in range(m):
        s, e, t = map(int, input().split())
        graph[s].append((e, t))
        graph[e].append((s, t))

    # 웜홀은 방향이 O
    for i in range(w):
        s, e, t = map(int, input().split())  # 줄어드는 시간
        graph[s].append((e, -t))

    result = [0 for _ in range(n+1)]
    answer = bf(i)

    print('YES' if answer else 'NO')
'''
1
3 2 1
1 2 3
2 3 4
3 1 8
'''