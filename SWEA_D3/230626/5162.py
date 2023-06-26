# 5162. 두가지 빵의 딜레마
# Level D3
# Site: https://swexpertacademy.com/main/code/problem/problemList.do

T = int(input())
for tc in range(1, T + 1):
    a, b, c = map(int, input().split())
    cost = min(a, b)
    answer = c // cost
    print(f'#{tc} {answer}')
