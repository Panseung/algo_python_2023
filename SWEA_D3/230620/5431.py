# 5431. 민석이의 과제 체크하기
# Level D3
# Site: https://swexpertacademy.com/main/code/problem/problemList.do

T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    students = list(map(int, input().split()))
    visited = [0] * N
    for s in students:
        visited[s - 1] = 1

    print(f'#{tc}', end=' ')
    for i in range(len(visited)):
        if not visited[i]:
            print(i + 1, end=' ')
    print()
