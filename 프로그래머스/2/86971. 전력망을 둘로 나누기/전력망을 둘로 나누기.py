from collections import deque, Counter

def solution(n, wires):
    answer = int(1e9)
    root=[i for i in range(n+1)]

    def union(root, x,y):
        rx=find(root, x)
        ry=find(root, y)
        if rx < ry:
            update_component(root, ry, rx)
        elif ry < rx:
            update_component(root, rx, ry)
    
    def find(root, x):
        if root[x]!=x:
            root[x]=find(root, root[x])
        return root[x]
    
    def update_component(root, old_root, new_root):
        for i in range(len(root)):
            if root[i] == old_root:
                root[i] = new_root
    
    for idx,wire in enumerate(wires):
        tmp=root[:]
        x,y=wire
        for idx2, wire2 in enumerate(wires):
            if idx==idx2: continue
            a,b=wire2
            union(tmp, a,b)
        
        cnt=list(Counter(tmp[1:]).values())
        answer=min(answer, abs(cnt[1]-cnt[0]))
        
    return answer