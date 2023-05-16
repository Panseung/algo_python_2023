# 1926. 간단한 369게임
# Level D2
# Site: https://swexpertacademy.com/main/code/problem/problemList.do

N = int(input())

answer = '1'
for i in range(2, N + 1):
    num = str(i)
    clap_cnt = 0
    for n in num:
        n = int(n)
        if n and n % 3 == 0:
            clap_cnt += 1
    if clap_cnt:
        clap = '-' * clap_cnt
        answer += ' ' + clap
    else:
        answer += ' ' + str(num)

print(answer)
