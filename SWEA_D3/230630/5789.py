# 5789. 현주의 상자 바꾸기
# Level D3
# Site: https://swexpertacademy.com/main/code/problem/problemList.do

T = int(input())
for tc in range(1, T + 1):
    N, Q = map(int, input().split())
    answer = [0] * N
    for num in range(1, Q + 1):
        l, r = map(int, input().split())
        for i in range(l - 1, r):
            answer[i] = num

    print(f'#{tc}', end=' ')
    print(*answer)
