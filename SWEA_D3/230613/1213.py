# 1213. String
# Level D3
# Site: https://swexpertacademy.com/main/code/problem/problemList.do

for tc in range(1, 11):
    input()
    word = input()
    words = input()
    answer = 0
    for i in range(len(words) - len(word) + 1):
        if words[i:i + len(word)] == word:
            answer += 1

    print(f'#{tc} {answer}')
