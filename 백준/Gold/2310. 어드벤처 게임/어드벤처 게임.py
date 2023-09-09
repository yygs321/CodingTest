from collections import defaultdict, deque


def dfs(num, money):
    global result
    elt = graph[num][0]
    cost = int(graph[num][1])
    rooms = graph[num][2:]

    if elt == 'L':
        if money < cost:
            money = cost
    elif elt == 'T':
        if money < cost:
            return
        else:
            money -= cost

    if num == n:
        result = 1  # 한번이라도 통과하는 경우가 있으면 성공
        return

    visited[num] = True
    for room in rooms:
        if visited[int(room)] == True:
            continue
        dfs(int(room), money)
    visited[num] = False


while True:
    n = int(input())
    if n == 0:
        break

    graph = defaultdict(list)
    for i in range(1, n+1):
        graph[i] = list(input().split())[:-1]

    visited = [False for _ in range(n+1)]

    result = 0
    dfs(1, 0)

    if result == 0:
        print("No")
    else:
        print("Yes")