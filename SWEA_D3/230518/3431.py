# 3431. 준환이의 운동관리
# Level D3
# Site: https://swexpertacademy.com/main/code/problem/problemList.do

T = int(input())
for tc in range(1, T + 1):
    L, U, X = map(int, input().split())
    answer = 0
    if X < L:
        answer = L - X
    elif X > U:
        answer = -1
    print(f'#{tc} {answer}')
