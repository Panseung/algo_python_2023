# 11856. 반반
# Level D3
# Site: https://swexpertacademy.com/main/code/problem/problemList.do

T = int(input())
for tc in range(1, T + 1):
    word = input()
    answer = 'No'
    lst = list()
    for w in word:
        if w not in lst:
            lst.append(w)

    if len(lst) == 2:
        if word.count(lst[0]) == 2 and word.count(lst[1]) == 2:
            answer = 'Yes'

    print(f'#{tc} {answer}')
