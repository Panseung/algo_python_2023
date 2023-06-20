# 1216. 회문2
# Level D3
# Site: https://swexpertacademy.com/main/code/problem/problemList.do

for _ in range(10):
    tc = int(input())
    brd = [input() for _ in range(100)]
    rotated_brd = []
    for x in range(100):
        line = ''
        for y in range(100):
            line += brd[y][x]
        rotated_brd.append(line)
    length = 100
    while True:
        find = False
        for y in range(100):
            for x in range(101 - length):
                word = brd[y][x:x + length]
                if word == word[::-1]:
                    find = True
                    break
            if find:
                break
        if find:
            break

        for y in range(100):
            for x in range(101 - length):
                word = rotated_brd[y][x:x + length]
                if word == word[::-1]:
                    find = True
                    break
            if find:
                break
        if find:
            break
        length -= 1

    print(f'#{tc} {length}')
