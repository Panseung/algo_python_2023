# 11736. 평범한 숫자
# Level D3
# Site: https://swexpertacademy.com/main/code/problem/problemList.do

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    lst = list(map(int, input().split()))
    answer = 0
    for i in range(N - 2):
        mini_lst = lst[i:i + 3]
        if lst[i + 1] != max(mini_lst) and lst[i + 1] != min(mini_lst):
            answer += 1

    print(f'#{tc} {answer}')
