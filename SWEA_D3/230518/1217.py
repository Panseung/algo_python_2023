# 1217. 거듭 제곱
# Level D3
# Site: https://swexpertacademy.com/main/code/problem/problemList.do

for _ in range(10):
    tc = int(input())
    N, M = map(int, input().split())
    print(f'#{tc} {N ** M}')
