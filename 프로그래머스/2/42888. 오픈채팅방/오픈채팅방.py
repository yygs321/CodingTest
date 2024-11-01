def solution(record):
    result = []
    answer=[]
    dict={}
    for rc in record:
        rc_lst=list(rc.split(" "))
        behavior=rc_lst[0]
        user_id=rc_lst[1]
        if len(rc_lst)==3:
            name=rc_lst[2]
        if user_id not in dict:
            dict[user_id]=""
            
        if behavior=='Enter':
            dict[user_id]=name
            result.append((0,user_id))
        elif behavior=='Leave':
            result.append((1,user_id))
        elif behavior=='Change':
            dict[user_id]=name
            
    for rs in result:
        inout, user_id=rs
        if inout==0:
            answer.append(dict[user_id]+"님이 들어왔습니다.")
        else:
            answer.append(dict[user_id]+"님이 나갔습니다.")
            
    return answer