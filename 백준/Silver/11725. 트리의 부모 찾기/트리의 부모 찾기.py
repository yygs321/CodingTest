from collections import deque
from collections import defaultdict

N=int(input())
start=1

lst=defaultdict(list)
result=defaultdict(list)
stack=deque()
visited=[]
result=defaultdict(list)
parent=1

for _ in range(N-1):
    x,y=map(int,input().split())  
    lst[x].append(y)
    lst[y].append(x)

def dfs(stack,parent):
    stack=[parent]
    result[1]=1
    while stack:
        s=stack.pop()
        for ls in lst[s]:
            if result[ls]==[]:
                result[ls]=s
                stack.append(ls)
                        
dfs(stack,parent)

#defaultdict 라서 value로 가져와야함
for i in range(2,N+1):
    print(result[i])