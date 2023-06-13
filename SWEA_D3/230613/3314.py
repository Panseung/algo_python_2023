# 3314. 보충학습과 평균
# Level D3
# Site: https://swexpertacademy.com/main/code/problem/problemList.do

t = int(input())
for tc in range(1, t + 1):
    scores = list(map(int, input().split()))

    sumV = 0
    for score in scores:
        sumV += max(40, score)

    print(f'#{tc} {sumV // 5}')