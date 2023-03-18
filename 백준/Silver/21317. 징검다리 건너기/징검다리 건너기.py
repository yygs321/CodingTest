#에너지의 최솟값=bfs
#n개의 돌
#+1, +2, +3(한번)
from collections import defaultdict

n=int(input())
stone=[0]*(n+1)
small=[0 for _ in range(n+1)]
big=[0 for _ in range(n+1)]

for i in range(1,n):
    s,b=map(int,input().split())
    small[i]=s
    big[i]=b
#+3 때의 에너지
k=int(input())

flag=0
energy=0
answer=1e9

def dfs(num, energy, flag):
    global answer
    if num>n:
        return
    if num==n:
        answer=min(answer, energy)
        return
  
    #+1 넘어가는 경우
    dfs(num+1, energy+small[num], flag)
    #+2 넘어가는 경우
    dfs(num+2, energy+big[num], flag)
  
    if flag==0:
        flag=1
        dfs(num+3, energy+k, flag)


dfs(1, energy, flag)
print(answer)