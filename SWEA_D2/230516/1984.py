# 1984. 중간 평균값 구하기
# Level D2
# Site: https://swexpertacademy.com/main/code/problem/problemList.do

T = int(input())
for tc in range(1, T + 1):
    lst = list(map(int, input().split()))
    lst.sort()
    lst = lst[1:9]
    answer = round(sum(lst) / 8)
    print(f'#{tc} {answer}')