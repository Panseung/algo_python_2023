# 1983. 조교의 성적 매기기
# Level D2
# Site: https://swexpertacademy.com/main/code/problem/problemList.do

T = int(input())
scores = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    score_lst = []
    for i in range(N):
        a, b, c = map(int, input().split())
        score_lst.append([i, a * 35 + b * 45 + c * 20])
    score_lst.sort(key=lambda x: x[1], reverse=True)

    same_cnt = N // 10
    score_idx = 0
    for i in range(0, N, same_cnt):
        for j in range(same_cnt):
            score_lst[i + j].append(scores[score_idx])
        score_idx += 1
    score_lst.sort(key=lambda x: x[0])

    print(f'#{tc} {score_lst[K - 1][2]}')
