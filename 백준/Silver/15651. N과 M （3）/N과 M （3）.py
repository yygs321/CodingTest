def comb(cnt):
  global n
  global m
  if cnt==m:
    print(*lst)
    return

  for i in range(1,n+1):
    lst.append(i)
    comb(cnt+1)
    lst.pop()


n,m=map(int,input().split())
lst=[]
comb(0)