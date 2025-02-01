from collections import defaultdict
import heapq
import sys
sys.setrecursionlimit(10**6)

def solution(n, paths, gates, summits):
    graph = defaultdict(list)
    
    gates = set(gates)
    summits = set(summits)
    
    for s, e, d in paths:
        graph[s].append((e, d))
        graph[e].append((s, d))

    dp = [float('inf')] * (n + 1)
    tmp = float('inf')
    answer = -1

    # BFS를 사용하여 최소 경로의 최대값을 구함
    def bfs(gate):
        nonlocal tmp, answer
        queue = []
        heapq.heappush(queue, (0, gate))
        dp[gate] = 0

        while queue:
            cur_d, cur = heapq.heappop(queue)

            # 현재 값이 dp값보다 크면 더 이상 진행할 필요 없음
            if cur_d > dp[cur]:
                continue

            # summits에 도달한 경우
            if cur in summits:
                # tmp보다 더 큰 값은 무시
                if tmp < cur_d:
                    continue
                # tmp와 같은 값일 경우, summit 번호가 더 큰 값은 무시
                if tmp == cur_d and answer < cur:
                    continue
                answer = cur
                tmp = cur_d
                continue

            # 인접 노드 탐색
            for nxt, nxt_d in graph[cur]:
                if nxt in gates:
                    continue

                new_d = max(cur_d, nxt_d)
                if new_d < dp[nxt]:
                    dp[nxt] = new_d
                    heapq.heappush(queue, (new_d, nxt))

    # 모든 gate에서 BFS 탐색 시작
    for gate in gates:
        bfs(gate)

    return [answer, tmp]
