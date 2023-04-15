#9019

#d: n*2 %10000
#s: n-1 / 0이면 9999
#l: n의 각 자리수를 왼편으로 회전 (deque.rotate(-1))
#r: 각 자리수를 오른편으로 회전

#a를 b로 바꾸는 최소한의 명령어
from collections import deque

def left(n):
    front=n%1000
    back=n//1000
    x=front*10+back
    return x

def right(n):
    front=n//10
    back=n%10
    x=back*1000+front
    return x

def bfs():
    global b
    while queue:
        a, result=queue.popleft()
        if a==b:
            print(*result, sep="")
            return
    
        a2=(a*2)%10000
        if a2 not in visited:
            visited.add(a2)
            queue.append((a2,result+"D"))
    
        if a==0: #a-1==0일때로 하면 a=0인 경우의 D,S,L,R확인 불가
            a2=9999
        else:
            a2=a-1
        if a2 not in visited:
            visited.add(a2)
            queue.append((a2,result+"S"))
   
        a2=left(a)
        if a2 not in visited:
            visited.add(a2)
            queue.append((a2, result+"L"))
  
        a2=right(a)
        if a2 not in visited:
            visited.add(a2)
            queue.append((a2, result+"R"))
      

T=int(input())
for tc in range(T):
    result=""
    queue=deque()
    visited=set() #list in 시간복잡도 O(n), set in 시간복잡도 O(1)
      
    a,b=map(int,input().split())
    queue.append((a,result))
    visited.add(a)
    bfs()