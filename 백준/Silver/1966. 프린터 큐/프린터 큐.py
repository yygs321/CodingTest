import sys
from collections import deque
input=sys.stdin.readline

n=int(input())

for _ in range(n):
  answer=0
  m,idx=map(int,input().split())
  priority=list(map(int,input().split(' ')))

  queue=[i for i in range(m)]
  dic={i:p for i,p in enumerate(priority)}
  while queue:
    key=queue.pop(0)
    value=dic.get(key)

    if value>=max(dic.values()):
      answer+=1
      del dic[key]
      if key==idx:
        print(answer)
        break
    else:
      queue.append(key)


    
  