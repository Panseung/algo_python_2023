# 1209. Sum
# Level D3
# Site: https://swexpertacademy.com/main/code/problem/problemList.do

for _ in range(10):
    tc = int(input())
    brd = [list(map(int, input().split())) for _ in range(100)]
    brd2 = []
    for x in range(100):
        line = []
        for y in range(100):
            line.append(brd[y][x])
        brd2.append(line)

    answer = 0
    for i in range(100):
        maxV = max(sum(brd[i]), sum(brd2[i]))
        if maxV > answer:
            answer = maxV

    cross1, cross2 = 0, 0
    for i in range(100):
        cross1 += brd[i][i]
        cross2 += brd2[i][i]

    answer = max(answer, cross2, cross1)

    print(f'#{tc} {answer}')
