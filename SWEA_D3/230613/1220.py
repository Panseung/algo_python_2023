# 1220. Magnetic
# Level D3
# Site: https://swexpertacademy.com/main/code/problem/problemList.do

for tc in range(1, 11):
    N = int(input())
    brd = [list(map(int, input().split())) for _ in range(100)]

    cnt = 0
    for x in range(100):
        floor = 0
        for y in range(100):
            if brd[y][x] == 1:
                floor = y
                break

        res = 1
        while floor < 100:
            res_num = brd[floor][x]
            if res_num and res_num != res:
                if res == 1:
                    res = 2
                    cnt += 1
                else:
                    res = 1
            floor += 1

    print(f'#{tc} {cnt}')