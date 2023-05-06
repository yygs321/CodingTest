n=int(input())
graph=[list(map(int,input().split())) for _ in range(n)]

#1번 전봇대로 정렬
graph.sort(key=lambda x:x[0])

LIS=[1 for _ in range(n)]
#최장 증가수열
for i in range(n):
    for j in range(i):
        if graph[j][1]<graph[i][1]:
            LIS[i]=max(LIS[i], LIS[j]+1)

print(n-max(LIS))