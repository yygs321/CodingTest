#1965
from bisect import bisect_left

n=int(input())
lst=list(map(int,input().split()))

result=[0]
answer=0
for ls in lst:
  if result[-1]<ls:
    result.append(ls)
  else:
    x=bisect_left(result,ls)
    result[x]=ls
    
print(len(result)-1)