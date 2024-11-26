def solution(picks, minerals):
    # 사용할 수 있는 최대 광물 수
    max_minerals = sum(picks) * 5
    minerals = minerals[:max_minerals]  # 캘 수 있는 만큼만 자르기

    # 광물 5개씩 묶어서 카운트
    groups = [[0, 0, 0] for _ in range(10)]
    for i, mineral in enumerate(minerals):
        if mineral == 'diamond':
            groups[i // 5][0] += 1
        elif mineral == 'iron':
            groups[i // 5][1] += 1
        else:
            groups[i // 5][2] += 1

    # 피로도가 높은 순으로 정렬
    groups.sort(key=lambda x: (-x[0], -x[1], -x[2]))

    # 피로도 계산
    answer = 0
    for group in groups:
        d, i, s = group
        if picks[0] > 0:  # 다이아 곡괭이
            picks[0] -= 1
            answer += d + i + s
        elif picks[1] > 0:  # 철 곡괭이
            picks[1] -= 1
            answer += 5 * d + i + s
        elif picks[2] > 0:  # 돌 곡괭이
            picks[2] -= 1
            answer += 25 * d + 5 * i + s

    return answer