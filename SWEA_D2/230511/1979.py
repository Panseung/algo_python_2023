# 1979. 어디에 단어가 들어갈 수 있을까
# Level D2
# Site: https://swexpertacademy.com/main/code/problem/problemList.do

T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    answer = 0
    brd = []
    brd.append([0] * (N + 2))  # 맨 윗줄에 빈 칸 0 채워주기
    for _ in range(N):
        lst = list(map(int, input().split()))
        lst.insert(0, 0)  # 행 앞 뒤로 빈 칸 0 채워주기
        lst.append(0)
        brd.append(lst)
    brd.append([0] * (N + 2))  # 맨 아랫줄에 빈 칸 0 채워주기

    for width in brd:
        for i in range(N + 2 - K):
            if width[i] == 0 and sum(width[i + 1: i + 1 + K]) == K and width[i + K + 1] == 0:
                answer += 1
    for i in range(N + 2):  # 세로
        height = []
        for j in range(N + 2):
            height.append(brd[j][i])
        for k in range(N + 2 - K):
            if height[k] == 0 and sum(height[k + 1: k + 1 + K]) == K and height[k + K + 1] == 0:
                answer += 1
    print(f'#{tc} {answer}')
