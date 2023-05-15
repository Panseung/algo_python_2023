# 1940. 가랏! RC카!
# Level D2
# Site: https://swexpertacademy.com/main/code/problem/problemList.do

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    lst = []
    for _ in range(N):
        lst.append(list(map(str, input().split())))

    answer1 = []
    answer2 = []
    answer3 = []

    for x in range(N):
        line = ''
        for y in range(N - 1, -1, -1):
            line += (lst[y][x])
        answer1.append(line)

    for y in range(N - 1, -1, -1):
        line = ''
        for x in range(N - 1, -1, -1):
            line += (lst[y][x])
        answer2.append(line)

    for x in range(N - 1, -1, -1):
        line = ''
        for y in range(N):
            line += (lst[y][x])
        answer3.append(line)

    answer = [answer1, answer2, answer3]

    print(f'#{tc}')
    for n in range(N):
        for a in answer:
            print(a[n], end=' ')
        print()
