# 1970. 쉬운 거스름돈
# Level D2
# Site: https://swexpertacademy.com/main/code/problem/problemList.do


money_lst = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    answer = []
    for m in money_lst:
        answer.append(N // m)
        N = N % m

    print(f'#{tc}')
    print(*answer)
