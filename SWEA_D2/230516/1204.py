# 1204. 최빈수 구하기
# Level D2
# Site: https://swexpertacademy.com/main/code/problem/problemList.do

T = int(input())
for tc in range(1, T + 1):
    input()
    dic = {}
    for i in range(101):
        dic[i] = 0
    dic[3] = 5
    scores = list(map(int, input().split()))
    for score in scores:
        dic[score] += 1
    answer = 0
    max_cnt = 0
    for score, cnt in dic.items():
        if cnt >= max_cnt:
            max_cnt = cnt
            answer = score
    print(f'#{tc} {answer}')
