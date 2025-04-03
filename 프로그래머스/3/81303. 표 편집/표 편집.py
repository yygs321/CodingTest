def solution(n, k, cmd):
    answer = ["O"] * n
    deleted = []
    prev = {i: i - 1 for i in range(n)}  # 이전 행 연결
    next = {i: i + 1 for i in range(n)}  # 다음 행 연결
    next[n - 1] = -1  # 마지막 행의 다음을 -1로 설정
    prev[0] = -1  # 첫 번째 행의 이전을 -1로 설정

    for c in cmd:
        action = c.split()
        
        if action[0] == "U":
            x = int(action[1])
            for _ in range(x):
                k = prev[k]

        elif action[0] == "D":
            x = int(action[1])
            for _ in range(x):
                k = next[k]

        elif action[0] == "C":
            answer[k] = "X"
            deleted.append((k, prev[k], next[k]))

            if prev[k] != -1:
                next[prev[k]] = next[k]
            if next[k] != -1:
                prev[next[k]] = prev[k]

            k = next[k] if next[k] != -1 else prev[k]

        elif action[0] == "Z":
            z, prev_row, next_row = deleted.pop()
            answer[z] = "O"

            if prev_row != -1:
                next[prev_row] = z
            if next_row != -1:
                prev[next_row] = z

    return "".join(answer)