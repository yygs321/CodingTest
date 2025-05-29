def solution(picks, minerals):
    fatigue_table = [[1, 1, 1], [5, 1, 1], [25, 5, 1]]
    mineral_index = {'diamond': 0, 'iron': 1, 'stone': 2}
    minerals=[mineral_index[x] for x in minerals]

    n = len(minerals)
    max_rounds = (n + 4) // 5

    answer = float('inf')

    def dfs(current_picks, round_num, fatigue):
        nonlocal answer

        # 종료 조건: 라운드 초과 또는 곡괭이 소진
        if round_num == max_rounds or sum(current_picks) == 0:
            answer = min(answer, fatigue)
            return

        for pick in range(3):
            if current_picks[pick] == 0:
                continue

            current_picks[pick] -= 1

            tmp = 0
            start = round_num * 5
            end = min(start + 5, n)

            for mineral in minerals[start:end]:
                tmp += fatigue_table[pick][mineral]

            dfs(current_picks, round_num + 1, fatigue + tmp)
            current_picks[pick] += 1  # 백트래킹 복원

    dfs(picks[:], 0, 0)
    return answer
