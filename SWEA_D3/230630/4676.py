# 4676. 늘어지는 소리 만들기
# Level D3
# Site: https://swexpertacademy.com/main/code/problem/problemList.do

T = int(input())
for tc in range(1, T + 1):
    answer = input()
    n = int(input())
    idx_lst = list(map(int, input().split()))
    idx_lst.sort()
    
    answer_lst = []
    for a in answer:
        answer_lst.append(a)

    for i in range(n):
        idx = idx_lst[i] + i
        answer_lst.insert(idx, '-')

    result = ''
    for a in answer_lst:
        result += a
    print(f'#{tc} {result}')
