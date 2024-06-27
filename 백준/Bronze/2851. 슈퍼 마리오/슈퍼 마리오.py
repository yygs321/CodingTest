score_list = []
answer = 0

for _ in range(10):
    score_list.append(int(input()))

for score in score_list:
    if abs(100-answer) >= abs(100-(answer+score)):
        answer += score
    else:
        break

print(answer)