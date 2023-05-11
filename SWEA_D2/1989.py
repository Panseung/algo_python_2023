# 1989. 초심자의 회문 검사
# Level D2
# Site: https://swexpertacademy.com/main/code/problem/problemList.do

T = int(input())
for t in range(1, T + 1):
    word = input()
    answer = 1
    for i in range(len(word) // 2):
        if word[i] != word[-i - 1]:
            answer = 0
            break

    print(f'#{t} {answer}')
