from collections import defaultdict
from itertools import combinations
import copy

n = int(input())
graph = [list(input().split()) for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
number = 0
dic = defaultdict(tuple)
in_dic = set()


# 선생님 주변에 학생이 바로 있는 경우는 예외 처리
def neighbor(x, y):
    for k in range(4):
        nx = x+dx[k]
        ny = y+dy[k]
        if nx < 0 or ny < 0 or nx >= n or ny >= n:
            break
        if graph[nx][ny] == 'S':
            return False
    return True


# 감시 시뮬레이션: 한 방향으로 감시할 때 학생이 보이는지
def watch(x, y, d, board):
    while True:
        nx = x + dx[d]
        ny = y + dy[d]

        if nx < 0 or ny < 0 or nx >= n or ny >= n:
            break
        if board[nx][ny] == 'O':  # 장애물이 있으면 시야 차단
            break
        if board[nx][ny] == 'S':  # 학생 발견
            return True
        x, y = nx, ny

    return False


# 학생 감시되는지 전체 확인
def detect(board):
    for i in range(n):
        for j in range(n):
            if board[i][j] == 'T':
                for d in range(4):
                    if watch(i, j, d, board):
                        return True
    return False


# 장애물 설치 가능한 위치 저장
for i in range(n):
    for j in range(n):
        if graph[i][j] == 'X':
            dic[number] = (i, j)
            number += 1
        elif graph[i][j] == 'T':
            if not neighbor(i, j):
                print("NO")
                exit()


for combi in combinations(dic.keys(), 3):
    visited = copy.deepcopy(graph)
    for c in combi:
        i, j = dic[c]
        visited[i][j] = 'O'

    if not detect(visited):  # 감시 피함
        print("YES")
        exit()

print("NO")
