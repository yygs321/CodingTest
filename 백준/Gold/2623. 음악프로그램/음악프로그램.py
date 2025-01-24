from collections import deque
n,m=map(int,input().split())

line=[0 for _ in range(n+1)]
pds_front=[[] for _ in range(n+1)]
pds_back=[[] for _ in range(n+1)]
answer=[]

for _ in range(m):
    tmp=list(map(int,input().split()))[1:]

    for idx, val in enumerate(tmp):
        pds_back[val]+=tmp[idx+1:]
        if idx==0: continue
        pds_front[val]+=tmp[:idx]

for idx,pd in enumerate(pds_front):
    line[idx]=len(set(pd))
pds_back=[set(pd) for pd in pds_back]

def dfs():
    queue=deque()
    for idx, val in enumerate(line):
       if idx==0: continue
       if val==0:
           queue.append(idx)

    while queue:
        x=queue.popleft()
        answer.append(x)

        for pd in pds_back[x]:
            line[pd]-=1

            if line[pd]==0:
                queue.append(pd)

    return

dfs()
if sum(line)!=0:
    print(0)
else:
    print(*answer, sep='\n')