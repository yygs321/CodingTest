from bisect import bisect_left
def solution(n, t, m, timetable):
    answer = ''
    timetable.sort()
    new_timetable=[]
    for time in timetable:
        hh,mm=map(int,time.split(':'))
        hh*=60
        new_timetable.append(hh+mm)
    
    current_time=540 #60*9 : 9시
    con_time=0
    arrived=0
    while n>0:
        n-=1
        idx=bisect_left(new_timetable, current_time)
        
        #마지막 운행일때
        if n==0: 
            #맨 마지막 사람보다 버스 시간이 뒤일 경우
            if idx>=len(new_timetable): 
                #사람이 남아있으면
                if arrived+m<=len(new_timetable):
                    #다음 차례 사람보다 1분 빨리
                    con_time=new_timetable[arrived+m-1]-1       
                #사람이 남아있지 않으면 콘이 타면 됨
                else:
                    con_time=current_time
                
            
            #마지막 시간이 무조건 전체 사람 이후(모두가 탈 수 있음)
            else:
                #현재 타고 있는 사람 수가 현재 시간에 탈 수 있는 사람 수보다 많을 때
                if idx>arrived+m:
                    #탈 수 있는 맨 마지막 사람보다 1분빨리
                    con_time=new_timetable[arrived+m-1]-1

                #현재 타고 있는 사람 수가 탈 수 있는 사람수와 같을 때
                elif idx==arrived+m:
                    #(타고 있고=탈 수 있는) 맨 마지막 사람보다 빨리
                    con_time=new_timetable[arrived+m-1]-1

                #현재 타고 있는 사람 수가 탈 수 있는 사람 수보다 적을 때
                else: # idx < arrived+m
                    if new_timetable[idx]==current_time: #딱 출발 시간이면 그보다 빨리
                        con_time= new_timetable[idx]-1
                    else: #idx 위치값이 출발시간 보다 뒷타임이면 => 자리 비어있음
                        con_time=current_time
                        
            arrived=min(idx,arrived+m)
            break

        #버스 시간이 탑승 가능한 맨마지막 사람보다 앞일 때(인원은 되는데 시간이 늦음)
        #이부분 뭐지???
        elif idx<arrived+m-1:
            arrived=idx #탄 사람만
        arrived+=m #다음 가능한 수
        current_time+=t
    
    con_h=con_time//60
    con_m=con_time%60
    answer=answer="{:02d}:{:02d}".format(con_h, con_m)
    return answer