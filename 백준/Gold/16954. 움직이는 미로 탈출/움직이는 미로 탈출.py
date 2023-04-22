from collections import deque

def down(cnt,graph):
    cnt+=1
    tmp=graph[:]
    tmp.insert(0, ['.' for _ in range(8)])
    tmp.pop()
    return (cnt,tmp)

def solve():
    x,y=7,0

    queue.append((x,y,graph,0))

    while queue:
        x,y,gp,c=queue.popleft()

        if (c and c >= x) or (x==0 and y==7):
            print(1)
            return


        cnt,tmp=down(c,gp)
        flag=0
        for i in range(9):
            nx=x+dx[i]
            ny=y+dy[i]
            if i==8 and flag:
                continue

            if nx<0 or nx>=8 or ny<0 or ny>=8: continue
            if gp[nx][ny]=='#': continue

            if tmp[nx][ny]!='#':
                flag=1
                queue.append((nx,ny,tmp,cnt))


        if flag==0 and not queue:
            print(0)
            return



graph=[list(input().rstrip()) for _ in range(8)]
dx=[-1,1,0,0,1,1,-1,-1,0]
dy=[0,0,-1,1,1,-1,1,-1,0]


queue=deque()
solve()

