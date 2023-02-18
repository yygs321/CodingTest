import sys

# N 입력받기
N = int(input())


current =0
stack=[0]
answer=[]

# 수열 입력받기
for _ in range(N):
    
    # Boundary Condition (stack, current, target)
    target = int(sys.stdin.readline().strip())
    
    # (+) When current < target
    while current < target:
        current += 1
        stack.append(current)
        answer.append('+')

        # Current = Target 에 도달했을 때 마지막 값을 빼줌
        if current ==target:
            stack.pop()
            answer.append('-')

    # Current 값이 Target 값보다 작은 경우 
    if current > target:

        #오름차순 수열에 위반되는 경우 i.e current > target인데, Push(+)가 수행되는 경우
        if stack[-1] < target:
            stack.append(-1)
            break

        while stack[-1] >= target:
            stack.pop()
            answer.append('-')

# 답 출력
if len(stack) !=1:
    answer = 'NO'
    print(answer)

else:
    for method in answer:
        print(method)