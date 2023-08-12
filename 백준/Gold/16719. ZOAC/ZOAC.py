# 가장 작은 것 기준 오른쪽 먼저 완성
# 그 이후 왼쪽 완성
# dfs

lst = list(input().rstrip())
result = ["" for _ in range(len(lst))]


def solution(start, lst):
    if not lst:  # 빈 리스트
        return

    # 남은 리스트에서 가장 작은 값 찾기
    min_val = min(lst)
    temp = lst.index(min_val)

    result[start + temp] = min_val
    print("".join(result))

    # 오른쪽 먼저 재귀 -> 가장 최소인 값의 오른쪽부터 다 출력
    solution(start+temp+1, lst[temp+1:])
    # 오른쪽이 완성된 상태로 왼쪽 출력
    solution(start, lst[:temp])


solution(0, lst)