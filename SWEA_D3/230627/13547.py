# 13547. 팔씨름
# Level D3
# Site: https://swexpertacademy.com/main/code/problem/problemList.do

T = int(input())
for tc in range(1, T + 1):
    k = input()
    win = 0
    answer = 'YES'
    for ox in k:
        if ox == 'o':
            win += 1
    if 15 - len(k) < 8 - win:
        answer = 'NO'

    print(f'#{tc} {answer}')
