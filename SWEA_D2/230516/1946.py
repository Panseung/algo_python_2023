# 1946. 간단한 압축 풀기
# Level D2
# Site: https://swexpertacademy.com/main/code/problem/problemList.do

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    answer = ''
    for _ in range(N):
        alpha, cnt = input().split()
        answer += alpha * int(cnt)

    print(f'#{tc}')
    for i in range(0, len(answer), 10):
        print(answer[i: i + 10])
