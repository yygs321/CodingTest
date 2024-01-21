def find(x):
    if x==parent[x]:
        return x
    parent[x] = find(parent[x])
    return parent[x]

def union(a,b):
    a=find(a)
    b=find(b)
    if a<b:
        parent[b]=a
    else:
        parent[a]=b


n,m = map(int,input().split())
graph = [list(input().strip()) for _ in range(n)]

parent = [i for i in range(n*m)]

direction = dict()
direction['D']=[1,0]
direction['L']=[0,-1]
direction['R']=[0,1]
direction['U']=[-1,0]

for num in range(n*m): 
    #  num : 각 배열의 고유 번호일때 행,열 값
    x = num//m
    y = num%m
    cur = graph[x][y]

    nx = x+direction[cur][0]
    ny = y+direction[cur][1]    
    next_num = nx*m + ny

    if next_num<0 or next_num >= n*m:continue

    union(num,next_num)

answer = 0
visited = set()
for i in range(n*m):
    if find(parent[i]) not in visited:
        answer+=1
        visited.add(find(parent[i]))
print(answer)