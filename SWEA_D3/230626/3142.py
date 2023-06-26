# 3142. 영준이와 신비한 뿔의 숲
# Level D3
# Site: https://swexpertacademy.com/main/code/problem/problemList.do

T = int(input())
for tc in range(1, T + 1):
    n, m = map(int, input().split())

    one = m * 2 - n
    two = m - one

    print(f'#{tc} {one} {two}')
