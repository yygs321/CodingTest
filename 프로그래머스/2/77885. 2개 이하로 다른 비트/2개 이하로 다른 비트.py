def solution(numbers):
    answer=[]
    for num in numbers:
        bin_num=[0]+list(map(int,bin(num)[2:]))
        idx=list(reversed(bin_num)).index(0)
        l=len(bin_num)-1
        
        if idx>=l: #0이 없는 경우
            answer.append(num+2**(l-1))
        elif idx==0: #0이 제일 끝에 있는 경우
            answer.append(num+1)
        else: #0이 가운데 끼인 경우
            answer.append(num+2**(idx-1))
            
    return answer