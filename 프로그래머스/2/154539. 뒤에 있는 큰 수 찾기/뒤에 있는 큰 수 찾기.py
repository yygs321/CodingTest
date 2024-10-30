def solution(numbers):
    stack=[]
    answer = []
    for num in numbers[::-1]:
        while True:
            if not stack:
                stack.append(num)
                answer.append(-1)
                break
            if num>=stack[-1]:
                stack.pop()
            else:
                answer.append(stack[-1])
                stack.append(num)
                break

    return answer[::-1]