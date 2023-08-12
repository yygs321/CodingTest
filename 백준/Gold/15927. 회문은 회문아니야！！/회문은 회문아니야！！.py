# left, right 이동하면서 찾으려했지만 실패
# 회문 -> 회문 길이 -1 이 답
# 회문인데 전부 같으면 -1

lst = input().rstrip()

left = 0
right = len(lst)-1


def palindrome(lst):
    if lst != lst[::-1]:  # 팰린드롬 아니면
        return len(lst)
    else:
        # 회문인데 전부 같은 문자인 경우
        if len(set(lst)) == 1:
            return -1
        else:
            # 회문이면 하나 없앤 값이 답
            return len(lst)-1


answer = palindrome(lst)

print(answer)