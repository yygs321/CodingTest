from collections import deque,defaultdict

def solution(enroll, referral, seller, amount):
    answer = []
    reference=defaultdict(list)
    money=defaultdict(int)
    for e,r in zip(enroll,referral):
        if r=="-":
            r="minho"
        reference[e].append(r)
    
    total=defaultdict(int)
    for s,a in zip(seller,amount):
        queue=deque([(s,a*100)])

        while queue:
            cur,x=queue.popleft()
            if x*0.1<1:
                money[cur]+=x
                break
            remain=int(x*0.1)
            money[cur]+=(x-remain)

            for nxt in reference[cur]:
                queue.append((nxt,remain))
        
    for e in enroll:
        answer.append(money[e])
         
    return answer

