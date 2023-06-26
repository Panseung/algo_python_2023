# 14555. 공과 잡초
# Level D3
# Site: https://swexpertacademy.com/main/code/problem/problemList.do

T = int(input())
for tc in range(1, T + 1):
    land = input()

    idx = 0
    answer = 0
    while idx < len(land):
        if land[idx] == '(':
            idx += 1
            answer += 1
        elif land[idx] == ')':
            answer += 1

        idx += 1

    print(f'#{tc} {answer}')
