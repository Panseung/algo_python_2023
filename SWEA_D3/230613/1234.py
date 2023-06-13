# 1234. 비밀번호
# Level D3
# Site: https://swexpertacademy.com/main/code/problem/problemList.do

for tc in range(1, 11):
    n, pw = input().split()

    while True:
        again = 0

        for i in range(len(pw) - 1):
            if pw[i] == pw[i + 1]:
                new_pw = ''
                new_pw += pw[0:i]
                new_pw += pw[i+2:len(pw)]
                pw = new_pw
                again = 1
                break

        if not again:
            break

    print(f'#{tc} {pw}')
