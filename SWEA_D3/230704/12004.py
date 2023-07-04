# 12004. 구구단 1
# Level D3
# Site: https://swexpertacademy.com/main/code/problem/problemList.do

def divider(num):
    div = 9
    while div >= 1:
        if num % div == 0 and num / div <= 9:
            return 'Yes'
        else:
            div -= 1
    return 'No'


TC = int(input())
for tc in range(1, TC + 1):
    print(f'#{tc} {divider(int(input()))}')
