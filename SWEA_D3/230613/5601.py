# 5601. 쥬스 나누기
# Level D3
# Site: https://swexpertacademy.com/main/code/problem/problemList.do

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    print(f'#{tc}', end=' ')
    for _ in range(N):
        print(f'1/{N}', end=' ')
    print()
