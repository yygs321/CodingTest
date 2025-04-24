from collections import defaultdict

def solution(gems):
    n = len(set(gems))
    count = defaultdict(int)
    result = [0, len(gems)]
    l = 0

    for r in range(len(gems)):
        count[gems[r]] += 1

        # r이 늘어났을 때 l로 구간 줄여가면서 가능한 최단 구간 구하기
        while len(count) == n:
            if r - l < result[1] - result[0]:
                result = [l, r]

            count[gems[l]] -= 1
            if count[gems[l]] == 0:
                del count[gems[l]]
            l += 1

    return [result[0] + 1, result[1] + 1]
