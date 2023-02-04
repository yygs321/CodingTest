def count(num):
    #개수를 센 수의 길이 : 1~9: 1 / 10~99: 2...
    if num<=1:
        same=0
    elif num<10:
        same=1
    elif num<100:
        same=2
    elif num<1000:
        same=3
    
    return same

def solution(s):
    answer=1005
    if len(s)<=1: 
        return len(s)
    
    for i in range(1,(len((s))//2)+1):
        ls=""
        cnt=1
        result=0
        for j in range(0,len(s),i):
            if j==0:
                ls=s[j:j+i]
                continue
                
            if ls==s[j:j+i]:
                cnt+=1
                if len(s[j:])==i: #마지막에 값이 같을 경우
                    same=count(cnt)
                    result+=same
                    result+=i
                    break
                continue
            #값이 다른경우
            
            #개수를 센 수의 길이 : 1~9: 1 / 10~99: 2...
            same=count(cnt)
            #앞의 값들 개수
            result+=same
            result+=i
            cnt=1
            
            ls=s[j:j+i]
            
            if len(s[j:])<=i: #값이 다른데 마지막일경우
                result+=len(s[j:])
                continue

        answer=min(answer, result)
                   
    return answer