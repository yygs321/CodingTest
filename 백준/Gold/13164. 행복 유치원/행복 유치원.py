import heapq

n, k = map(int, input().split())
childrens = list(map(int, input().split()))

height = []
for i in range(1, n):
    heapq.heappush(height, childrens[i]-childrens[i-1])

answer = 0

# n-k 개 만큼의 키차이를 무시할 수 있음(다른 조로 나눠버리기)
for i in range(n-k):
    answer += heapq.heappop(height)

print(answer)
