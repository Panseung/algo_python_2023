# 6692. 다솔이의 월급 상자
# Level D3
# Site: https://swexpertacademy.com/main/code/problem/problemList.do

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    answer = 0
    for _ in range(N):
        a, b = map(float, input().split())
        answer += a * b

    print(f'#{tc} {round(answer, 6)}')
