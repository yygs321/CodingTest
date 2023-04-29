import sys
input=sys.stdin.readline

n=int(input())
lst=sorted(list(map(int,input().split())))
minV=float('inf')
answer=[]

def solve(n):
    global minV
    global answer
    tmp=[]
  
    for i in range(n-2):
        left=i+1
        right=n-1
  
        while left<right:
            tmp=[lst[i],lst[left],lst[right]]
    
            if minV>abs(sum(tmp)):
                minV=abs(sum(tmp))
                answer=tmp[:]
              
            if sum(tmp) >0:
                right-=1
            elif sum(tmp) <0: 
                left+=1
            else: #0이면
                answer=tmp[:]
                return answer
    return answer

answer=solve(n)
print(*sorted(answer))