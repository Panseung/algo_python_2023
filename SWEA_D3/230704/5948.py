# 5948. 새샘이의 7-3-5 게임
# Level D3
# Site: https://swexpertacademy.com/main/code/problem/problemList.do

T = int(input())
for tc in range(1, T + 1):
    lst = list(map(int, input().split()))
    sum_lst = list()
    for i in range(5):
        for j in range(1, 6):
            for k in range(2, 7):
                if i == j or j == k or i == k:
                    continue
                sum_lst.append(lst[i] + lst[j] + lst[k])
    sum_lst = list(set(sum_lst))
    sum_lst.sort(reverse=True)
    print(f'#{tc} {sum_lst[4]}')
