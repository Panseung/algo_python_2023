# 1859. 백만 장자 프로젝트
# Level D2
# Site: https://swexpertacademy.com/main/code/problem/problemList.do

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    lst = list(map(int, input().split()))

    rest_idx = 0
    max_price = max(lst)
    max_idx = lst.index(max_price)
    answer = 0
    while rest_idx < N:
        if rest_idx == max_idx:
            lst = lst[rest_idx + 1::]
            if len(lst) == 0:
                break
            N -= rest_idx + 1
            max_price = max(lst)
            max_idx = lst.index(max_price)
            rest_idx = 0
            continue
        answer += max_price - lst[rest_idx]
        rest_idx += 1

    print(f'#{tc} {answer}')
