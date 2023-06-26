# 14692. 통나무 자르기
# Level D3
# Site: https://swexpertacademy.com/main/code/problem/problemList.do

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    answer = 'Alice'
    if N % 2:
        answer = 'Bob'

    print(f'#{tc} {answer}')
