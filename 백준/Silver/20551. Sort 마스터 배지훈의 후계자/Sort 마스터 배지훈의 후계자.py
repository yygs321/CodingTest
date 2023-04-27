#question이 alist에서 가장 먼저 등장한 위치 출력
#존재하지 않으면 -1

n,m=map(int,input().split())
alist=[]
for _ in range(n):
    alist.append(int(input()))

question=[]
for _ in range(m):
    question.append(int(input()))

alist.sort()

def bin(start, end, v):
    if start>end: 
        result.append(-1)
        return

    mid=(start+end)//2
  
    if alist[mid]==v:
        result.append(alist.index(v))
        return
      
    if v<alist[mid]:
        bin(start, mid-1, v)
    else:
        bin(mid+1, end, v)
  

result=[]
find={}
for i,q in enumerate(question):
    if q in find:
        result.append(find[q])
        continue
    bin(0, n-1, q)
    find[q]=result[i]

print(*result, sep="\n")