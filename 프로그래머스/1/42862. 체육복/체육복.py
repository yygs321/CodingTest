def solution(n, lost, reserve):
    answer = 0
    student=[0]*(n+1)
    for i in range(1,n+1):
        if i in lost and i in reserve:
            student[i]=1
        elif i in lost:
            student[i]=0
        elif i in reserve:
            student[i]=2
        else:
            student[i]=1
    
    for i in range(1,n+1):
        if student[i]==0:
            if student[i-1]==2:
                student[i-1]=1
                student[i]=1
                continue
            if i<n:
                if student[i+1]==2:
                    student[i+1]=1
                    student[i]=1
                
    answer=n-student[1:].count(0)
        
    return answer