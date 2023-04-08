def comb(cnt, start):
  global m
  if cnt==m:
    print(*result)
    return

  last=0
  for i in range(start, len(lst)):
    if i in selectedIdx or last==lst[i]: continue
    result.append(lst[i])
    selectedIdx.append(i)
    last=lst[i]
    comb(cnt+1, i+1)
    selectedIdx.pop()
    result.pop()


n,m=map(int,input().split())
lst=sorted(list(map(int,input().split())))
selectedIdx=[]
result=[]

comb(0,0)