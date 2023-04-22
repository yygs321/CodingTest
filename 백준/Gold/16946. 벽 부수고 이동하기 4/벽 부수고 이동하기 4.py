from collections import defaultdict, deque

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

N, M = map(int, input().split())

graph = []

dic = defaultdict(int)

empty_graph = [[0 for i in range(M)] for j in range(N)]

for _ in range(N):
    graph.append(input())

q = deque()
num = 1

for row in range(N):
    for col in range(M):
        if graph[row][col] == '1':  # 벽이면 통과
            continue
        if empty_graph[row][col] != 0:  # 이미 방문했으면 통과
            continue

        max_value = 0
        q.append((row, col))
        empty_graph[row][col] = num

        while q:
            c_row, c_col = q.popleft()
            max_value += 1
            for i in range(4):
                n_row = c_row + dr[i]
                n_col = c_col + dc[i]
                if n_row < 0 or n_col < 0 or n_row >= N or n_col >= M:
                    continue
                if graph[n_row][n_col] == '1':  # 벽이면 통과
                    continue
                if empty_graph[n_row][n_col] != 0:  # 이미 방문했으면 통과
                    continue
                empty_graph[n_row][n_col] = num
                q.append((n_row, n_col))

        dic[num] = max_value

        num += 1

answer = [[0 for i in range(M)] for j in range(N)]
# print(empty_graph)
for row in range(N):
    for col in range(M):
        #print(row, col)
        # print(graph[row][col])
        if graph[row][col] == '0':
            answer[row][col] = 0
        else:
            # print("wall")
            s = set()
            for i in range(4):
                n_row = row + dr[i]
                n_col = col + dc[i]
                if n_row < 0 or n_col < 0 or n_row >= N or n_col >= M:
                    continue
                #print("row,col", n_row, n_col)
                s.add(empty_graph[n_row][n_col])
            for i in s:
                answer[row][col] += dic[i] % 10
            # print(s)
            answer[row][col] += 1
            answer[row][col] = answer[row][col] % 10

for i in range(N):
    print(''.join(str(s) for s in answer[i]))