from itertools import permutations as p

INF = int(1e9)

# 알파벳이 주어졌을 때 상하로 움직이는 횟수 구하는 함수
def countChange(alp):
	return min(ord('Z') - ord(alp) + 1, ord(alp) - ord('A'))

# 왼쪽, 오른쪽 중 최단으로 가는 거리 구하는 함수
def findShortestPath(name, now, next):
    right, left = max(next, now), min(next, now)
    rightDist = right - left
    leftDist = left + len(name) - right
    return min(rightDist, leftDist)

def solution(name):
    answer = INF
    # "A" 가 아니라서 가야하는 위치(시작 위치 제외)
    toGoPlaces = [i for i in range(len(name)) if name[i] != "A" and i != 0]

    # 알파벳을 바꾸느라 생기는 이동
    changeCount = 0
    for c in name:
        changeCount += countChange(c);

    # 움직일 수 있는 모든 케이스
    cases = p(toGoPlaces, len(toGoPlaces))
    for case in cases:
        now = 0
        result = 0

        for next in case:
            dist = findShortestPath(name, now, next)
            result += dist
            now = next
            
        answer = min(answer, result + changeCount)

    return answer