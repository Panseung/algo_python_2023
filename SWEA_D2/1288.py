# 1288. 새로운 불면증 치료법
# Level D2
# Site: https://swexpertacademy.com/main/code/problem/problemList.do

T = int(input())
for t in range(1, T + 1):
    N = int(input())
    rest_num = 0
    visited = [0] * 10
    while sum(visited) < 10:
        rest_num += N
        for n in str(rest_num):
            visited[int(n)] = 1

    print(f'#{t} {rest_num}')
