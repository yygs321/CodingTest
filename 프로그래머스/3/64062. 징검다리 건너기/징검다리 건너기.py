from collections import deque

def solution(stones, k):
    answer = float('inf')
    dq = deque()
    
    for i in range(len(stones)):
        # 윈도우 벗어난 인덱스 제거
        while dq and dq[0] <= i - k:
            dq.popleft()
        # (뒤에서부터) 현재 값보다 작거나 같은 값은 모두 제거
        while dq and stones[dq[-1]] <= stones[i]:
            dq.pop()
        dq.append(i)
        # 윈도우 시작 시점부터 결과 계산
        if i >= k - 1:
            answer = min(answer, stones[dq[0]])
    
    return answer
