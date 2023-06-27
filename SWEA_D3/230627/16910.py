# 16910. 원 안의 점
# Level D3
# Site: https://swexpertacademy.com/main/code/problem/problemList.do

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    answer = 1
    answer += N * 4
    valid_spot = 0
    for y in range(1, N):
        for x in range(1, N):
            if y ** 2 + x ** 2 <= N ** 2:
                valid_spot += 1
    answer += valid_spot * 4

    print(f'#{tc} {answer}')
