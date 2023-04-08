def perm(cnt):
  if cnt==m:
    print(*result)
    return

  for i in range(len(lst)):    
    if not isSelected[i]:
      isSelected[i]=True
      result.append(lst[i])
      perm(cnt+1)
      isSelected[i]=False
      result.pop()
  

n,m=map(int,input().split())
lst=sorted(list(map(int,input().split())))
result=[]
isSelected=[False]*n
perm(0)