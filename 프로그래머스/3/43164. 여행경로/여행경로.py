from collections import defaultdict

def solution(tickets):
    def dfs(start, path):
        if len(path) == len(tickets) + 1:
            answer.append(path)  # 리스트를 복사해서 저장
            return
        
        for i, next in enumerate(dict[start]):
            dict[start].pop(i)
            dfs(next, path+[next])
            dict[start].insert(i, next)
            
    answer = []
    
    dict=defaultdict(list)
    for s,e in tickets:
        if dict[s]:
            dict[s].append(e)
            continue
            
        dict[s]=[e]
        
    dfs('ICN', ['ICN'])
    
    answer.sort()
        
    return answer[0]