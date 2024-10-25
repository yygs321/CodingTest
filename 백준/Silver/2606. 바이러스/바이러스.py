from collections import deque

n=int(input())
m=int(input())
root=[i for i in range(n+1)]
def union(x,y):
    root_x, root_y= find(x), find(y)
    if root_x<root_y:
        root[y]=root_x
    else:
        root[x]=root_y

def find(x):
    if root[x]!=x:
        root[x]=find(root[x])
    return root[x]

computer=[[] for _ in range(n+1)]
for _ in range(m):
    a,b=map(int,input().split())
    computer[a].append(b)
    computer[b].append(a)

queue=deque()
queue.append(1)
cnt=0
done=set()
done.add(1)
while queue:
    q=queue.popleft()

    for next in computer[q]:
        if next in done:
            continue
        union(q,next)
        cnt+=1
        done.add(next)
        queue.append(next)
    
print(cnt)