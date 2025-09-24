from itertools import combinations

def solution(n, q, ans):
    answer = 0
    
    for perm in combinations(range(1,n+1),5):
        for i, query in enumerate(q):
            if len(set(perm)&set(query))!=ans[i]:
                break
        else:
             answer+=1  
                
    return answer