#시간복잡도를 줄이기 위해 heap 사용
import heapq
n=int(input())
hp=[]
result=0

#값을 모두 받아온 후에 계산 따로
for i in range(n):
    heapq.heappush(hp, int(input()))

while len(hp)>1:
    #hp에 들어있는 값중 계속해서 최소값 2개가 나오는 것
    x1=heapq.heappop(hp)
    x2=heapq.heappop(hp)

    result+=x1+x2
    heapq.heappush(hp,x1+x2)
    
print(result)