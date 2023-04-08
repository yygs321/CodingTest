def comb(cnt):
  global m
  if cnt==m:
    print(*result)
    return

  last=0
  for i in range(len(lst)):
    if last==lst[i]: continue
    result.append(lst[i])
    last=lst[i]
    comb(cnt+1)
    result.pop()


n,m=map(int,input().split())
lst=sorted(list(map(int,input().split())))
result=[]

comb(0)