def comb(cnt, start):
  if cnt==m:
    print(*result)
    return

  for i in range(start, len(lst)):
    result.append(lst[i])
    comb(cnt+1, i+1)
    result.pop()
  

n,m=map(int,input().split())
lst=sorted(list(map(int,input().split())))
result=[]

comb(0,0)