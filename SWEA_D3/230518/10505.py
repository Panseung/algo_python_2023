# 10505. 소득 불균형
# Level D3
# Site: https://swexpertacademy.com/main/code/problem/problemList.do

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    lst = list(map(int, input().split()))
    lst.sort()
    mean = sum(lst) // len(lst)

    answer = 0
    for num in lst:
        if num <= mean:
            answer += 1
        else:
            break
    print(f'#{tc} {answer}')
