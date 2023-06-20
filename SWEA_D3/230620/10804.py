# 10804. 문자열의 거울상
# Level D3
# Site: https://swexpertacademy.com/main/code/problem/problemList.do

dic = {'b': 'd', 'd': 'b', 'p': 'q', 'q': 'p'}

T = int(input())
for tc in range(1, T + 1):
    word = input()
    answer = ''
    for w in word:
        answer += dic[w]
    print(f'#{tc} {answer[::-1]}')
