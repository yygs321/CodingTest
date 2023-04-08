def comb(cnt):
  if cnt==m:
    print(*result)
    return

  for i in range(0, len(lst)):
    if result and result[-1]>lst[i]: continue
    result.append(lst[i])
    comb(cnt+1)
    result.pop()
      

n,m=map(int,input().split())
lst=sorted(list(map(int,input().split())))
result=[]
comb(0)