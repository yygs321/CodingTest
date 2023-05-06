from bisect import bisect_left

n=int(input())
graph=list(map(int,input().split()))
LIS=[graph[0]]


for i in range(n):
    if LIS[-1]>=graph[i]:
        idx=bisect_left(LIS, graph[i]) #위치 찾고
        LIS[idx]=graph[i] #값 업데이트

    else: #더 큰값나오면 추가: 길이 +1
        LIS.append(graph[i])

print(len(LIS))