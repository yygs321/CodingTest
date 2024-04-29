import heapq
from collections import deque
        
def solution(n, costs):
    
    def union(x,y):
        a=find(x)
        b=find(y)

        if a==b:
            return False #사이클 발생
        
        if a<b:
            root[b]=a
        else:
            root[a]=b
        return True

    def find(x):
        if root[x]!=x:
            root[x]=find(root[x])
        return root[x]
    
    
    root=[i for i in range(n)]
    costs.sort(key=lambda x:x[2])
    answer = 0
    
    for cost in costs:
        s,e,v=cost
        
        if union(s,e): #사이클 발생안하면
            answer+=v
    
    return answer