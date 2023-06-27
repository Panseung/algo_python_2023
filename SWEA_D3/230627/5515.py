# 5515. 2016년 요일 맞추기
# Level D3
# Site: https://swexpertacademy.com/main/code/problem/problemList.do

months = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30]

T = int(input())
for tc in range(1, T + 1):
    m, d = map(int, input().split())
    d += 3
    for i in range(m - 1):
        d += months[i]

    print(f'#{tc} {d % 7}')
