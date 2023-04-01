#서류, 면접 두개가 모두 나보다 잘난 사람이 있으면 안됨
#선발가능한 최대 인원 수
import heapq

test=int(input())
for tc in range(test):
    n=int(input())
    employee=[]
    cnt=1 #1등은 무조건 채용
  
    for i in range(n):
        #서류 성적, 면접 순위
        a,b=map(int,input().split())
        heapq.heappush(employee, (a,b))
  
    
    lst=[]
    idx=1
    a,b=heapq.heappop(employee)
    for i in range(1,n):
        a2,b2=heapq.heappop(employee) #a2가 a보다 서류점수는 낮은데

        if b2<b: #면접 점수는 b2가 더 높으면 
            a=a2
            b=b2
            cnt+=1
            continue
  
    print(cnt)