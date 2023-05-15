# 1940. 가랏! RC카!
# Level D2
# Site: https://swexpertacademy.com/main/code/problem/problemList.do

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    answer = 0
    rest_speed = 0
    for n in range(N):
        cmd = list(map(int, input().split()))
        if len(cmd) == 1:
            answer += rest_speed
        elif cmd[0] == 1:
            rest_speed += cmd[1]
            answer += rest_speed
        else:
            rest_speed = max(0, rest_speed - cmd[1])
            answer += rest_speed
    print(f'#{tc} {answer}')
