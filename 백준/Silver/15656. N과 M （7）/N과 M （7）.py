def perm(cnt):
  if cnt==m:
    print(*result)
    return

  for i in range(0, len(lst)):
    result.append(lst[i])
    perm(cnt+1)
    result.pop()
  

n,m=map(int,input().split())
lst=sorted(list(map(int,input().split())))
result=[]

perm(0)