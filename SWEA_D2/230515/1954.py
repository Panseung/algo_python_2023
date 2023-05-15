# 1954. 달팽이 숫자
# Level D2
# Site: https://swexpertacademy.com/main/code/problem/problemList.do

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]
T = int(input())
for tc in range(1, T + 1):
    N = int(input())

    answer = [[0 for _ in range(N)] for _ in range(N)]
    cnt = 0
    x, y, d = 0, 0, 0
    while cnt < N * N:
        cnt += 1
        answer[y][x] = cnt
        if y + dy[d] >= N or y + dy[d] < 0 or x + dx[d] >= N or x + dx[d] < 0 or answer[y + dy[d]][x + dx[d]] != 0:
            d = (d + 1) % 4
        y += dy[d]
        x += dx[d]

    print(f'#{tc}')
    for a in answer:
        print(*a)
