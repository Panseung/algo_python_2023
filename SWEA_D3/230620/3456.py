# 3456. 직사각형 길이 찾기
# Level D3
# Site: https://swexpertacademy.com/main/code/problem/problemList.do

T = int(input())
for tc in range(1, T + 1):
    a, b, c = map(int, input().split())
    answer = a
    if a == b:
        answer = c
    elif a == c:
        answer = b

    print(f'#{tc} {answer}')
