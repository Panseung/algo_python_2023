# 4299. 태혁이의 사랑은 타이밍
# Level D3
# Site: https://swexpertacademy.com/main/code/problem/problemList.do

d_time = 11 * 24 * 60 + 11 * 60 + 11

T = int(input())
for tc in range(1, T + 1):
    d, h, m = map(int, input().split())
    answer = d * 24 * 60 + h * 60 + m - d_time
    if answer < 0:
        answer = -1
    print(f'#{tc} {answer}')
