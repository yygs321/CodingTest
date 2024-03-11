def solution(msg):
    alpha='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    dict={}
    cnt=1
    for a in alpha:
        dict[a]=cnt
        cnt+=1
    answer = []
    idx=0
    
    while idx<len(msg):
        tmp=0
        while msg[idx:idx+tmp+1] in dict:
            tmp+=1
            if idx+tmp>len(msg):
                break
                
        x= msg[idx:idx+tmp]
        if x in dict:
            answer.append(dict[x])
        if msg[idx:idx+tmp+1] not in dict:
            dict[msg[idx:idx+tmp+1]]=cnt #없는 단어 추가
            cnt+=1
            
        idx+=tmp
        
    return answer