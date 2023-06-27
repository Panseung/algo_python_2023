# 3499. 퍼펙트 셔플
# Level D3
# Site: https://swexpertacademy.com/main/code/problem/problemList.do

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    middle = N // 2
    if N % 2:
        middle += 1
    lst = list(input().split())
    answer = []
    for i in range(middle):
        answer.append(lst[i])
        if i + middle < N:
            answer.append(lst[i + middle])

    print(f'#{tc}', end=' ')
    print(*answer)
