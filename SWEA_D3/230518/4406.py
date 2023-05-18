# 4406. 모음이 보이지 않는 사람
# Level D3
# Site: https://swexpertacademy.com/main/code/problem/problemList.do

vowel = ['a', 'e', 'i', 'o', 'u']
T = int(input())
for tc in range(1, T + 1):
    word = input()
    answer = ''
    for w in word:
        if w not in vowel:
            answer += w

    print(f'#{tc} {answer}')
