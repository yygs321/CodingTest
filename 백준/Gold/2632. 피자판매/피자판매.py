from collections import defaultdict

k = int(input())
n, m = map(int, input().split())
a = [int(input()) for _ in range(n)]
b = [int(input()) for _ in range(m)]


def partial_sum(pizza, length):
    # key: 부분합, val:각 부분합이 나타나는 횟수
    case = defaultdict(int)
    for i in range(length):
        # 피자 회전 (0-1-2-3-4/ 1-2-3-4-0)
        tmp = pizza[i:]+pizza[:i]
        key1 = 0
        for num in tmp:
            key1 += num
            case[key1] += 1  # key1을 만들 수 있는 횟수
    # 전체합은 따로 한번만
    case[sum(pizza)] = 1
    return case


caseA = partial_sum(a, n)
caseB = partial_sum(b, m)

answer = caseA[k]+caseB[k]  # 각 피자에서 만들어질 수 있는 횟수
# A와 B 피자 합쳐서 만들 수 있는 횟수
for ca in caseA:
    if k-ca in caseB:
        answer += caseA[ca]*caseB[k-ca]

print(answer)