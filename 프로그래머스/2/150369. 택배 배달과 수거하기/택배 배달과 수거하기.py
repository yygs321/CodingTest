def solution(cap, n, deliveries, pickups):
    answer=0
    deliver=0
    pick=0
    
    for i in range(n,0,-1):
        cnt=0
        # i번째 배달/수거를 끝내기 까지 몇번의 방문이 필요한지 체크
        while deliver < deliveries[i-1] or pick<pickups[i-1]:
            cnt+=1
            deliver+=cap
            pick+=cap
            
        deliver-=deliveries[i-1]
        pick-=pickups[i-1]
        answer+=i*cnt*2
            
    return answer