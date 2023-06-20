# 1228. 암호문1
# Level D3
# Site: https://swexpertacademy.com/main/code/problem/problemList.do

for tc in range(1, 11):
    N = int(input())
    pw_lst = list(map(int, input().split()))
    length = int(input())
    cmd = list(input().split())

    cnt = 0
    pos = 0
    while cnt < length:
        cnt += 1
        idx = int(cmd[pos + 1])
        l = int(cmd[pos + 2])
        pos += 3
        for i in range(l):
            pw_lst.insert(idx + i, cmd[pos + i])
        pos += l

    print(f'#{tc}', end=' ')
    print(*pw_lst[0:10])
