from collections import deque
n=int(input())
queue=deque()
for _ in range(n):
    request=input().split()

    if request[0]=='push':
        queue.append(request[1])
    elif request[0]=='pop':
        print(queue.popleft() if queue else -1)
    elif request[0]=='size':
        print(len(queue))
    elif request[0]=='empty':
        print(0 if queue else 1)
    elif request[0]=='front':
        print(queue[0] if queue else -1)
    elif request[0]=='back':
        print(queue[-1] if queue else -1)