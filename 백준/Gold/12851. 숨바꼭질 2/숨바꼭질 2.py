from collections import deque

n, k = map(int, input().split())
dist = [0 for _ in range(100001)]
queue = deque()
cnt = 0


def bfs():
    global cnt
    queue.append(n)

    while queue:
        x = queue.popleft()

        if x == k:
            cnt += 1
            continue

        for next in (x+1, x-1, 2*x):
            if next < 0 or next > 100000:
                continue
            # 방문하지 않았거나
            # 방문하더라도 현재 거리+1 보다 많거나 같게 움직인 곳 선택 -> 가장 짧은 거리
            if dist[next] == 0 or dist[next] >= dist[x]+1:
                dist[next] = dist[x]+1
                queue.append(next)


bfs()
print(dist[k])
print(cnt)