def solution(s):
    n = len(s)
    answer = 0

    for i in range(n):
        for j in range(n-1, i-1, -1):
            if s[i] == s[j]:
                if s[i:j+1] == s[i:j+1][::-1]:  # 여기만 제대로 검사
                    answer = max(answer, j - i + 1)
                    break

    return answer
