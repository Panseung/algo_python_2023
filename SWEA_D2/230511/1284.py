# 1284. 수도 요금 경쟁
# Level D2
# Site: https://swexpertacademy.com/main/code/problem/problemList.do

T = int(input())
for t in range(1, T + 1):
    P, Q, R, S, W = map(int, input().split())
    fee_A = W * P
    fee_B = Q + max(0, W - R) * S

    print(f'#{t} {min(fee_A, fee_B)}')
