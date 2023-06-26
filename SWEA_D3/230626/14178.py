# 14178. 1차원 정원
# Level D3
# Site: https://swexpertacademy.com/main/code/problem/problemList.do

T = int(input())
for tc in range(1, T + 1):
    N, D = map(int, input().split())
    valid_range = D * 2 + 1
    answer = N // valid_range
    if N % valid_range:
        answer += 1

    print(f'#{tc} {answer}')
