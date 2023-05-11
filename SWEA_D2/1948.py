# 1948. 날짜 계산기
# Level D2
# Site: https://swexpertacademy.com/main/code/problem/problemList.do

days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
T = int(input())
for tc in range(1, T + 1):
    m1, d1, m2, d2 = map(int, input().split())

    answer1 = d1
    for i in range(m1 - 1):
        answer1 += days[i]

    answer2 = d2
    for i in range(m2 - 1):
        answer2 += days[i]

    print(f'#{tc} {answer2 - answer1 + 1}')
