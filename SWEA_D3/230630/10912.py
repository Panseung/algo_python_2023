# 10912. 외로운 문자
# Level D3
# Site: https://swexpertacademy.com/main/code/problem/problemList.do

T = int(input())
for tc in range(1, T + 1):
    alpha_lst = [0] * 26
    words = input()
    for word in words:
        idx = ord(word) - 97
        if alpha_lst[idx]:
            alpha_lst[idx] = 0
        else:
            alpha_lst[idx] = 1

    answer = ''
    for i in range(26):
        idx = i + 97
        if alpha_lst[i]:
            answer += chr(idx)
    if answer == '':
        answer = 'Good'

    print(f'#{tc} {answer}')
