infix = list(input())
stack=[]
answer=''
for i in infix:
    if i.isalpha():
        answer+=i
    else:
        if i == '(':
            stack.append(i)
        elif i == '*' or i == '/':
            while stack and (stack[-1] == '*' or stack[-1] =='/'):
                answer += stack.pop()
            stack.append(i)
        elif i == '+' or i == '-':
            while stack and stack[-1] != '(':
                answer+= stack.pop()
            # (가 있을때는 우선순위가 높아짐
            stack.append(i)
        elif i == ')':
            while stack and stack[-1] != '(':
                answer += stack.pop()
            # (,)는 후위표기식에 필요없으므로 넣지않고 둘다 빼버림    
            stack.pop()
while stack :
    answer+=stack.pop()
print(answer)