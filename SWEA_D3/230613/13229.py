# 13229. 일요일
# Level D3
# Site: https://swexpertacademy.com/main/code/problem/problemList.do

days = ['', 'SAT', 'FRI', 'THU', 'WED', 'TUE', 'MON', 'SUN']

T = int(input())
for tc in range(1, T + 1):
    day = input()
    for i in range(8):
        if day == days[i]:
            print(f'#{tc} {i}')
            break
