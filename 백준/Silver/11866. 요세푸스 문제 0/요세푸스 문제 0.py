from collections import deque

n,k=map(int,input().split())
ycps=deque(i for i in range(1,n+1))
answer=[]
cnt=0

while ycps:
    q=ycps.popleft()
    cnt+=1
  
    if cnt==k:
        #제거
        answer.append(q)
        cnt=0
        continue
    ycps.append(q)

print("<",end="")
for i in range(len(answer)):
    if i==len(answer)-1: #마지막인덱스
        print("%d"%answer[i],end="")
        continue
    print("%d, " %answer[i] ,end="")
print(">")