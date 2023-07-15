from collections import deque

n, m = map(int, input().split())
students = [[] for _ in range(n+1)]
indegree = [0 for _ in range(n+1)]
for i in range(m):
    # a->b
    a, b = map(int, input().split())
    students[a].append(b)
    indegree[b] += 1

result = []


def solution():
    queue = deque()
    for i in range(1, n+1):
        if indegree[i] == 0:
            queue.append(i)

    while queue:
        x = queue.popleft()
        result.append(x)

        for student in students[x]:
            indegree[student] -= 1

            if indegree[student] == 0:
                queue.append(student)


solution()
print(*result)