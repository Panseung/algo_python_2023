# 10200. 구독자 전쟁
# Level D3
# Site: https://swexpertacademy.com/main/code/problem/problemList.do

T = int(input())
for tc in range(1, T + 1):
    N, A, B = map(int, input().split())
    only = min(A, B)
    both = max(0, A + B - N)

    print(f'#{tc} {only} {both}')
