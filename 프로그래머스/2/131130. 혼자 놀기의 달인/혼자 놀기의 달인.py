from collections import defaultdict,deque

def solution(cards):
    answer = 0
    n=len(cards)
    
    cards_idx=defaultdict(int)
    for idx,card in enumerate(cards):
        cards_idx[card]=idx+1
    
    result=[]
    visited=[False for _ in range(n+1)]
    for i in range(1,n+1):
        if visited[i]:
            result.append(0)
            continue
            
        queue=deque([i])
        visited[i]=True
        cnt=0
        while queue:
            cur=queue.popleft()
            cnt+=1
            
            nxt=cards_idx[cur]
            if visited[nxt]:
                break
            visited[nxt]=True
            queue.append(nxt)
        
        result.append(cnt)
        
    result.sort(reverse=True)
    answer=result[0]*result[1]
    
    return answer