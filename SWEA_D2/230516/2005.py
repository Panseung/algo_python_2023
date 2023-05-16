# 2005. 파스칼의 삼각형
# Level D2
# Site: https://swexpertacademy.com/main/code/problem/problemList.do

T = int(input())
for t in range(1, T + 1):
    N = int(input())

    cnt = 2
    brd = [[] for _ in range(N)]
    brd[0] = [1]
    while cnt <= N:
        for i in range(cnt):
            if 1 <= i < cnt - 1:
                num = brd[cnt - 2][i - 1] + brd[cnt - 2][i]
                brd[cnt - 1].append(num)
            else:
                brd[cnt - 1].append(1)
        cnt += 1

    print(f'#{t}')
    for line in brd:
        print(*line)
