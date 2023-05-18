# 11688. Calkin-Wilf tree 1
# Level D3
# Site: https://swexpertacademy.com/main/code/problem/problemList.do

T = int(input())
for tc in range(1, T + 1):
    cmd = input()

    l, r = 1, 1

    for c in cmd:
        if c == 'L':
            r += l
        else:
            l += r

    print(f'#{tc} {l} {r}')
