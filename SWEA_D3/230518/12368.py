# 12368. 24시간
# Level D3
# Site: https://swexpertacademy.com/main/code/problem/problemList.do

T = int(input())
for tc in range(1, T + 1):
    A, B = map(int, input().split())
    answer = (A + B) % 24

    print(f'#{tc} {answer}')
