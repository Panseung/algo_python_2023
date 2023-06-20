# 9700. USB 꽂기의 미스터리
# Level D3
# Site: https://swexpertacademy.com/main/code/problem/problemList.do

T = int(input())
for tc in range(1, T + 1):
    p, q = map(float, input().split())
    s1 = (1 - p) * q
    s2 = p * (1 - q) * q

    if s2 > s1:
        print(f'#{tc} YES')
    else:
        print(f'#{tc} NO')
