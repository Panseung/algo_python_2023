# 2805. 농작물 수확하기
# Level D3
# Site: https://swexpertacademy.com/main/code/problem/problemList.do

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    middle = N // 2
    answer = 0
    for i in range(N):
        gap = abs(i - middle)
        line = input()
        valid_line = line[gap:N - gap]
        for v in valid_line:
            answer += int(v)

    print(f'#{tc} {answer}')
