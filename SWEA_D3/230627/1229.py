# 1229. 암호문 2
# Level D3
# Site: https://swexpertacademy.com/main/code/problem/problemList.do

for tc in range(10):
    n = int(input())
    pw = list(map(int, input().split()))
    m = int(input())
    cmd = list(input().split())
    cmd.append('t')

    cnt = 0
    idx = 0
    while cnt < m:
        res_cmd = cmd[idx]
        idx += 1
        if res_cmd == 'D':
            for i in range(int(cmd[idx + 1])):
                if idx + 1 >= len(pw):
                    break
                del pw[int(cmd[idx])]
            idx += 2
        else:
            pos, num = int(cmd[idx]), int(cmd[idx + 1])
            idx += 2
            for i in range(num):
                pw.insert(pos + i, cmd[idx])
                idx += 1
        cnt += 1
    answer = pw[0:10]
    print(f'#{tc + 1}', end=' ')
    print(*answer)