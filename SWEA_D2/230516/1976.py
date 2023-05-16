# 1976. 시각 덧셈
# Level D2
# Site: https://swexpertacademy.com/main/code/problem/problemList.do

T = int(input())
for t in range(1, T + 1):
    h1, m1, h2, m2 = map(int, input().split())

    m = m1 + m2
    if m >= 60:
        h1 += 1
        m -= 60

    h = h1 + h2
    if h > 12:
        h -= 12

    print(f'#{t} {h} {m}')
