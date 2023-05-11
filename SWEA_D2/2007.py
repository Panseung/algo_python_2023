# 1959. 패턴 두 개의 숫자열
# Level D2
# Site: https://swexpertacademy.com/main/code/problem/problemList.do

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    n, m = min(N, M), max(N, M)
    A = list(list(map(int, input().split())))
    B = list(map(int, input().split()))

    if len(A) > len(B):
        A, B = B, A

    answer = 0
    for i in range(m - n + 1):
        sum_V = 0
        for j in range(n):
            sum_V += A[j] * B[j + i]
        answer = max(answer, sum_V)

    print(f'#{tc} {answer}')
