from collections import deque


def bfs():
    queue = deque()

    queue.append((1, 0, 0))

    while queue:
        q = queue.popleft()
        screen, copied, cnt = q

        if screen == s:
            return cnt

        for i in range(3):
            if i == 0:  # 복사
                screen_tmp, copied_tmp = screen, screen
            elif i == 1:  # 붙여넣기
                screen_tmp, copied_tmp = screen+copied, copied
            else:  # 한개 빼기
                screen_tmp, copied_tmp = screen-1, copied

            if screen_tmp >= 1001 or screen_tmp < 0:
                continue
            if copied_tmp >= 1001 or copied_tmp < 0:
                continue
            if visited[screen_tmp][copied_tmp]:
                continue

            visited[screen_tmp][copied_tmp] = True
            queue.append((screen_tmp, copied_tmp, cnt+1))


s = int(input())

# 화면 이모티콘 개수, 복사된 이모티콘 개수
visited = [[False for _ in range(1001)] for _ in range(1001)]
visited[1][0] = True
result = int(1e9)

result = min(result, bfs())
print(result)