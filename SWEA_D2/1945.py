# 1945. 간단한 소인수분해
# Level D2
# Site: https://swexpertacademy.com/main/code/problem/problemList.do

T = int(input())
for t in range(1, T + 1):
    N = int(input())
    numbers = [2, 3, 5, 7, 11]
    answers = []
    for num in numbers:
        cnt = 0
        while True:
            if N % num == 0:
                N = N / num
                cnt += 1
            else:
                break
        answers.append(cnt)
    print(f'#{t}', end=' ')
    print(*answers)
