# 1289. 원재의 메모리 복구하기
# Level D3
# Site: https://swexpertacademy.com/main/code/problem/problemList.do

T = int(input())
for tc in range(1, T + 1):
    memory = input()

    rest = '0'
    answer = 0
    for m in memory:
        if m != rest:
            rest = m
            answer += 1

    print(f'#{tc} {answer}')
