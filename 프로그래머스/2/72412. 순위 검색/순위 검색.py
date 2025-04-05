from collections import defaultdict
from bisect import bisect_left
def solution(info, query):
    answer = []
    dic=defaultdict(list)
    for i in info:
        i = i.split()
        for a in [i[0], '-']:
            for b in [i[1], '-']:
                for c in [i[2], '-']:
                    for d in [i[3], '-']:
                        dic[(a, b, c, d)].append(int(i[4]))

    # 지원자 점수 오름차순 정렬
    for k in dic:
        dic[k].sort()

    for qr in query:
        qr = qr.replace("and ", "")
        qr = qr.split()
        
        target_key = tuple(qr[:-1])
        target_score = int(qr[-1])
        
        cnt = 0
        target_list = dic[target_key]
        idx = bisect_left(target_list, target_score)
        cnt = len(target_list) - idx
        answer.append(cnt)      

    return answer