# 2001. 파리 퇴치
# Level D2
# Site: https://swexpertacademy.com/main/code/problem/problemList.do

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    brd = []
    for _ in range(N):
        brd.append(list(map(int, input().split())))

    answer = 0
    for y in range(N - M + 1):
        for x in range(N - M + 1):
            cnt = 0
            for m in range(M):
                cnt += sum(brd[y + m][x:x + M])
            if cnt > answer:
                answer = cnt
    print(f'#{tc} {answer}')
