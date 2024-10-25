from collections import deque
from collections import defaultdict

n=int(input())
m=int(input())
lst=defaultdict(list)
queue=deque()
visited=[False]*(n+1)
maxCnt=0
for _ in range(m):
    s,e=map(int,input().split())
    lst[s].append(e)
    lst[e].append(s)

def bfs(start):
    global maxCnt
    queue.append(start)
    visited[start]=True
  
    while queue:
        q= queue.popleft()
  
        for ls in lst[q]:
            if visited[ls]==False:
                visited[ls]=True
                maxCnt+=1
                queue.append(ls)

bfs(1)
print(maxCnt)

  
  