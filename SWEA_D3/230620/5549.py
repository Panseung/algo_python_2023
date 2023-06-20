# 5549. 홀수일까 짝수일까
# Level D3
# Site: https://swexpertacademy.com/main/code/problem/problemList.do

T = int(input())
for tc in range(1, T + 1):
    num = input()
    last = int(num[-1])
    answer = 'Even'
    if last % 2:
        answer = 'Odd'

    print(f'#{tc} {answer}')
