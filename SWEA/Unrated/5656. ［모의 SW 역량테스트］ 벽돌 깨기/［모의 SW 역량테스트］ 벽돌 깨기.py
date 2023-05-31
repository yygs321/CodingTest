# 남은 벽돌의 개수
from collections import deque
import copy


def perm(cnt):
    global answer
    global n
    if cnt == n:
        tmp = copy.deepcopy(graph)
        answer = min(answer, brick(lst, tmp))
        return

    for i in range(w):
        lst.append(i)
        perm(cnt+1)
        lst.pop()


def brick(lst, tmp):
    for ls in lst:
        for j in range(h):
            if tmp[j][ls] == 0:
                continue

            queue = deque()
            queue.append((j, ls, tmp[j][ls]))

            while queue:
                x, y, v = queue.popleft()

                tmp[x][y] = 0  # 본인 제거
                cnt = 1

                # 거리 v까지
                while cnt != v:
                    cnt += 1
                    for l in range(4):
                        nx = x+dx[l]*(cnt-1)
                        ny = y+dy[l]*(cnt-1)

                        if nx < 0 or nx >= h or ny < 0 or ny >= w:
                            continue
                        if tmp[nx][ny] == 0:
                            continue

                        queue.append((nx, ny, tmp[nx][ny]))
                        tmp[nx][ny] = 0

            # 벽돌 내려주기
            down(tmp)

            # 제일 위에 부딪힌값 찾고 break
            break

    # for i in range(h):
    #     print(*graph[i])
    # print("========")
    return count(tmp)


def down(tmp):
    global w
    global h
    # tmp=[[] for _ in range(w)]

    # 남은 벽돌
    for j in range(w):
        remains = []
        for i in range(h-1, -1, -1):
            if tmp[i][j] != 0:
                remains.append(tmp[i][j])
                tmp[i][j] = 0

        # 밑에서부터 채워주기
        index = -1
        for remain in remains:
            tmp[index][j] = remain
            index -= 1

    return


def count(tmp):
    global w
    global h
    cnt = 0
    for i in range(h):
        for j in range(w):
            if tmp[i][j] == 0:
                continue
            cnt += 1

    return cnt


T = int(input())
for tc in range(1, T+1):
    n, w, h = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(h)]
    lst = []
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    answer = int(1e9)
    perm(0)

    print(f'#{tc} {answer}')
