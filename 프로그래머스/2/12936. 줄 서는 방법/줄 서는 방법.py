def solution(n, k):
    # 팩토리얼 값 미리 구해놓기
    factorial = [1] * (n + 1)
    for i in range(1, n + 1):
        factorial[i] = factorial[i - 1] * i

    people = list(range(1, n + 1))
    answer = []
    k -= 1 #인덱스 값으로

    for i in range(n, 0, -1):
        fact = factorial[i - 1]     # (i-1)!
        idx = k // fact             # 몇 번째 그룹인지
        answer.append(people.pop(idx))
        k %= fact

    return answer
