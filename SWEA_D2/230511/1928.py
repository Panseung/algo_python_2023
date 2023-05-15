# 1986. 지그재그 숫자
# Level D2
# Site: https://swexpertacademy.com/main/code/problem/problemList.do

T = int(input())
for t in range(1, T + 1):
    N = int(input())
    answer = -1 * (N // 2)
    if N % 2:
        answer += N

    print(f'#{t} {answer}')
