def solution(edges):
    answer = [0, 0, 0, 0]

    inout = {}
    for a, b in edges:
        if not inout.get(a):
            inout[a] = [0, 0]
        if not inout.get(b):
            inout[b] = [0, 0]
        
        # [out, in] 카운팅
        inout[a][0] += 1
        inout[b][1] += 1
    
    for key, cnt in inout.items():
        # 생성점: out만 2개 이상, in 0 (조건이 그래프 수 합 2 이상이므로)
        if cnt[0] >= 2 and cnt[1] == 0:
            answer[0] = key
        # 막대그래프: out은 0, in 만 존재
        elif cnt[0] == 0 and cnt[1] > 0:
            answer[2] += 1
        # 8자 그래프: out, in 각각 2개 이상
        elif cnt[0] >= 2 and cnt[1] >= 2:
            answer[3] += 1
    
    # 도넛 그래프: 전체 그래프 개수인 생성점의 out 수 - 다른 그래프 개수
    answer[1] = (inout[answer[0]][0] - answer[2] - answer[3])

    return answer