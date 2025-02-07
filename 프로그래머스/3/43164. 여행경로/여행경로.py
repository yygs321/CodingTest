from collections import defaultdict
def solution(tickets):
    
    graph=defaultdict(list)
    num=0
    for ticket in tickets:
        s,e=ticket
        graph[s].append((e,num))
        num+=1
            
    
    def dfs(cur, path, visited):
        if False not in visited:
            result.append(path)
        
        for nxt,key in graph[cur]:
            if visited[key]==True:
                continue
                
            visited[key]=True
            dfs(nxt, path+[nxt], visited)
            visited[key]=False
    
    result=[]
    visited=[False]*(len(tickets))
    dfs("ICN", ["ICN"], visited)
    
    return sorted(result)[0]