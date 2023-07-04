# 5603. 건초더미
# Level D3
# Site: https://swexpertacademy.com/main/code/problem/problemList.do

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    lst = list()
    for _ in range(N):
        lst.append(int(input()))
    v = sum(lst) // N

    answer = 0
    for num in lst:
        answer += abs(num - v)

    print(f'#{tc} {answer // 2}')
