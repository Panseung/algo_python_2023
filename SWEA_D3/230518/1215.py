# 1215. 회문1
# Level D3
# Site: https://swexpertacademy.com/main/code/problem/problemList.do

for tc in range(1, 11):
    brd = []
    N = int(input())
    for _ in range(8):
        brd.append(list(input()))

    r_brd = [[] for _ in range(8)]
    for x in range(8):
        for y in range(8):
            r_brd[x].append(brd[y][x])

    answer = 0

    ry, rx = 0, 0
    while ry < 8:
        length = N // 2
        word = brd[ry][rx:rx + length]
        r_word = brd[ry][rx - 1 + N:rx - 1 + N - length:-1]
        if word == r_word:
            answer += 1

        word = r_brd[ry][rx:rx + length]
        r_word = r_brd[ry][rx - 1 + N:rx - 1 + N - length:-1]
        if word == r_word:
            answer += 1

        rx += 1
        if rx == 9 - N:
            rx = 0
            ry += 1

    print(f'#{tc} {answer}')
