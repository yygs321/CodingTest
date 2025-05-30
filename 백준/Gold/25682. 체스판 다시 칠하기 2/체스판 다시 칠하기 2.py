import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())

graph = []
for _ in range(n):
    graph.append([1 if ch == "B" else 0 for ch in input().rstrip()])

# 정답 패턴 (흑 시작, 백 시작)
blackwhite = [[[ (i + j) % 2 for j in range(m)] for i in range(n)],
              [[(i + j + 1) % 2 for j in range(m)] for i in range(n)]]

# 비교해서 다른 부분 1로 표시
def get_diff(board, pattern):
    return [[int(board[i][j] != pattern[i][j]) for j in range(m)] for i in range(n)]

diff_b = get_diff(graph, blackwhite[0])  # 흑 시작 기준 차이
diff_w = get_diff(graph, blackwhite[1])  # 백 시작 기준 차이

# 누적합 계산 함수
def get_prefix_sum(diff):
    s = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(n):
        for j in range(m):
            s[i+1][j+1] = s[i+1][j] + s[i][j+1] - s[i][j] + diff[i][j]
    return s

psum_b = get_prefix_sum(diff_b)
psum_w = get_prefix_sum(diff_w)

# 특정 구간 누적합 구하는 함수
def get_area(s, x1, y1, x2, y2):
    return s[x2][y2] - s[x1][y2] - s[x2][y1] + s[x1][y1]

# 최소 색칠 횟수 탐색
answer = float('inf')
for i in range(n - k + 1):
    for j in range(m - k + 1):
        cnt_b = get_area(psum_b, i, j, i + k, j + k)
        cnt_w = get_area(psum_w, i, j, i + k, j + k)
        answer = min(answer, cnt_b, cnt_w)

print(answer)
