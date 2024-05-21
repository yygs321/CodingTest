import math
# 출발점 -> 도착점, 일정한 속도
# 나는 특수 부스터 -> 첫 1초: Z 속도 -> 경주 시작 전 고를 수 있음 (Z<=Y)
# 나머지는 V[i]
# 단독우승이 가능한 최소의 Z 값
# 나는 n번 참가자

T = int(input())
lst = []
for tc in range(T):
    n, x, y = map(int, input().split())
    V = list(map(int, input().split()))
    max_result = x/max(V[:-1])
    mine = V[-1]
    answer = -1

    if x/mine < max_result:
        lst.append(0)
        continue

    for booster in range(y, 0, -1):
        if (x-booster)/mine + 1 < max_result:
            answer = booster

    lst.append(answer)

for l in lst:
    print(l)
