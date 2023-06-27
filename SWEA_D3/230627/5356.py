# 5356. 의석이의 세로로 말해요
# Level D3
# Site: https://swexpertacademy.com/main/code/problem/problemList.do

T = int(input())
for tc in range(1, T + 1):
    words = []
    max_len = 0
    for _ in range(5):
        word = input()
        words.append(word)
        if len(word) > max_len:
            max_len = len(word)

    answer = ''
    for i in range(max_len):
        for w in range(5):
            if len(words[w]) > i:
                answer += words[w][i]

    print(f'#{tc} {answer}')
