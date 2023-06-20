# 4751. 다솔이의 다이아몬드 장식
# Level D3
# Site: https://swexpertacademy.com/main/code/problem/problemList.do

T = int(input())
for tc in range(1, T + 1):
    S = input()
    first = '.'
    sec = '.'
    thr = '#'
    for i in range(len(S)):
        first += '.#..'
        sec += '#.#.'
        thr += f'.{S[i]}.#'
    print(first)
    print(sec)
    print(thr)
    print(sec)
    print(first)
