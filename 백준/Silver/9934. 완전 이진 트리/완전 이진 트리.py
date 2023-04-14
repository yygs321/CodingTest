from collections import deque
  
def bfs(lst):
  queue.append(lst)

  while queue:
      x=queue.popleft()
      if len(x)<1: break
      point=len(x)//2
  
      result.append(x[point])
      queue.append(x[:point])
      queue.append(x[point+1:])
    


k=int(input()) #높이 k
lst=list(map(int,input().split()))

queue=deque()
point=len(lst)
result=[]
bfs(lst)

cnt=0
z=1
for r in result:
    print(r, end=" ")
    if z==1 or cnt==z:
        print()
        z*=2
        cnt=0
    cnt+=1