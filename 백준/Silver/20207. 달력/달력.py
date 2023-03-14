#가장 많이 겹치는 날: 행
#일정이 떨어지지 않으면 열은 길어짐
from collections import deque

#일정개수
n=int(input())
lst=[0 for _ in range(366)] #0~365 

for i in range(n):
    s, e=map(int,input().split())
    for j in range(s,e+1):
        lst[j]+=1

flag=0
start=[]
for i in range(366):
    if lst[i]==0:
        flag=0
        continue

    if flag==0 and lst[i]!=0:
        flag=1
        start.append(i)

queue=deque()
def bfs(v):
    global r,c
  
    queue.append(v)
    c+=1
    
    while queue:
        q=queue.popleft()
        r=max(r, lst[q])

        if q+1<=365:
            if lst[q+1]!=0:
                c+=1
                queue.append(q+1)
                r=max(r, lst[q+1])
    
answer=0
r,c=0,0
for st in start:
    #초기화
    r=0
    c=0
    bfs(st)
  
    answer+= (r*c)

print(answer)