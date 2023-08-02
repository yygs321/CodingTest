import heapq
n,m=map(int,input().split())
score= list(map(int,input().split()))
heapq.heapify(score)

while m>0 and score:
    s1=heapq.heappop(score)
    s2=heapq.heappop(score)

    heapq.heappush(score, s1+s2)
    heapq.heappush(score, s1+s2)
    m-=1

if score:
    print(sum(score))
else:
    print(0)
