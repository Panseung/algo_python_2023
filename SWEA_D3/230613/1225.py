# 1225. 암호생성기
# Level D3
# Site: https://swexpertacademy.com/main/code/problem/problemList.do

from collections import deque

for tc in range(1, 11):
    int(input())
    pw = list(map(int, input().split()))

    min_num = min(pw)
    cycle = max(min_num // 15 - 1, 0)
    if cycle:
        decrease = cycle * 15
        for i in range(8):
            pw[i] -= decrease

    deq = deque(pw)
    dec = 0
    while True:
        dec += 1
        if dec > 5:
            dec = 1
        num = deq.popleft()
        num -= dec
        if num > 0:
            deq.append(num)
        else:
            deq.append(0)
            break
    print(f'#{tc}', end=' ')
    print(*deq)


