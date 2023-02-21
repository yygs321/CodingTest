N=int(input())
lst=[]
r,c=0,0
global answer
answer="" #밖에서 초기화해줘야함
for _ in range(N):
  graph=list(input())
  lst.append(graph)

def divide(r,c,size):
    global answer
    sum=0
    rEnd=r+size
    cEnd=c+size
    #범위 r,c부터인것 주의
    for i in range(r,rEnd): 
        for j in range(c,cEnd):
            sum+=int(lst[i][j])

    if sum==size*size:
        answer+="1"
    elif sum==0:
        answer+="0"
    else:
        answer+="("
        half=size//2
        if half<1 : return
        divide(r,c,half)
        divide(r,c+half,half)
        divide(r+half,c,half)
        divide(r+half,c+half,half)
        answer+=")"

divide(0,0,N)
print(answer)