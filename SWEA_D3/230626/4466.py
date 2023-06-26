# 4466. 최대 성적표 만들기
# Level D3
# Site: https://swexpertacademy.com/main/code/problem/problemList.do

T = int(input())

for tc in range(1, T + 1):
    N, K = map(int, input().split())
    score_lst = list(map(int, input().split()))
    score_lst.sort(reverse=True)

    sumV = 0
    for i in range(K):
        sumV += score_lst[i]

    print(f'#{tc} {sumV}')
