answer = int(1e9)
    
def solution(picks, minerals):

    # 다이아몬드, 철, 돌에 따른 피로도
    fatigue_values = [(1, 1, 1), (5, 1, 1), (25, 5, 1)]

    # DFS 함수 정의
    def dfs(depth, fatigue, usage):
        global answer

        # 모든 곡괭이 사용 완료 시 최소 피로도 갱신
        if depth == sum(picks):
            answer = min(answer, fatigue)
            return

        # 모든 곡괭이에 대해 탐색
        for i in range(3):
            # 해당 곡괭이 사용 가능 여부 확인
            if usage[i] < picks[i]:
                usage[i] += 1
                # 현재 곡괭이로 인한 피로도 계산
                plus = calculate_fatigue(depth, i)
                # 다음 곡괭이로 이동
                dfs(depth + 1, fatigue + plus, usage)
                usage[i] -= 1

        # 광물 종류에 따른 피로도 계산
    def calculate_fatigue(depth, index):
        start = depth * 5  # 현재 그룹의 시작 인덱스
        end = (depth + 1) * 5  # 현재 그룹의 끝 인덱스 (다음 그룹 시작 인덱스)
        plus = 0  # 피로도 누적 변수

        # 현재 그룹에서 광물을 순회하며 피로도 누적
        for mineral in minerals[start:end]:
            # 다이아몬드인 경우
            if mineral == "diamond":
                plus += fatigue_values[index][0]
            # 철광석인 경우
            elif mineral == "iron":
                plus += fatigue_values[index][1]
            # 돌인 경우
            else:  # stone
                plus += fatigue_values[index][2]

        return plus


    # 곡괭이 사용 횟수 기록
    usage = [0, 0, 0]
    # DFS 시작
    dfs(0, 0, usage)
    # 최소 피로도 반환
    return answer
