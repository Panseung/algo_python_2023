# 1974. 스도쿠 검증
# Level D2
# Site: https://swexpertacademy.com/main/code/problem/problemList.do

T = int(input())
for tc in range(1, T + 1):
    BRD = []
    for _ in range(9):
        BRD.append(list(map(int, input().split())))

    answer = 1
    for i in range(9):
        lst = [0] * 10
        lst[0] = 1
        for j in range(9):
            num = BRD[i][j]
            if lst[num]:
                answer = 0
                break
            else:
                lst[num] = 1
        if not answer:
            break

    for i in range(9):
        lst = [0] * 10
        lst[0] = 1
        for j in range(9):
            num = BRD[j][i]
            if lst[num]:
                answer = 0
                break
            else:
                lst[num] = 1
        if not answer:
            break

    y = 0
    x = 0
    while answer and y < 9:

        lst = [0] * 10
        lst[0] = 1
        for i in range(3):
            for j in range(3):
                num = BRD[x + i][y + j]
                if lst[num]:
                    answer = 0
                    break
                else:
                    lst[num] = 1
            if not answer:
                break
        x += 3
        if x == 9:
            x = 0
            y += 3

    print(f'#{tc} {answer}')
