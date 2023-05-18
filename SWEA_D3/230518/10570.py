# 10570. 제곱 팰린드롬 수
# Level D3
# Site: https://swexpertacademy.com/main/code/problem/problemList.do

answer = [0]
cnt = 0
for i in range(1, 1001):
    num = i ** 0.5
    if num == int(num):
        small, big = str(int(num)), str(i)

        if small == small[::-1] and big == big[::-1]:
            cnt += 1

    answer.append(cnt)

T = int(input())
for tc in range(1, T + 1):
    a, b = map(int, input().split())
    print(f'#{tc} {answer[b] - answer[a - 1]}')
