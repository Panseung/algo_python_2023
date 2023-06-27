# 1206. View
# Level D3
# Site: https://swexpertacademy.com/main/code/problem/problemList.do

for tc in range(1, 11):
    N = int(input())
    buildings = list(map(int, input().split()))
    answer = 0

    idx = 2
    while idx < N - 2:
        five_lst = buildings[idx - 2: idx + 3]
        five_lst.sort(reverse=True)
        if buildings[idx] == five_lst[0]:
            answer += five_lst[0] - five_lst[1]
            idx += 3
        else:
            idx += 1

    print(f'#{tc} {answer}')
