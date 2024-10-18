def solution(wallet, bill):
    answer = 0
    
    while True:
        if max(wallet)>=max(bill) and min(wallet)>=min(bill):
            break
        if bill[0]>bill[1]:
            bill.append(int(bill[0]/2))
            del bill[0]
        else:
            bill.append((int(bill[1]/2)))
            del bill[1]
        answer+=1
    return answer