def solution(n, computers):
    def union(x,y):
        if find(x)<find(y):
            for i in range(len(root)):
                if root[i]==root[x]:
                    root[i]=root[y]
        else:
            for i in range(len(root)):
                if root[i]==root[y]:
                    root[i]=root[x]
        
    def find(x):
        if root[x]!=x:
            root[x]=find(root[x])
        return root[x]
    
    root=[x for x in range(n)]
    for i, computer in enumerate(computers):
        for j in range(n):
            if i==j: continue
            if computers[i][j]==0: continue
            union(i,j)
        
    return len(set(root))