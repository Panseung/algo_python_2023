# 1221. GNS
# Level D3
# Site: https://swexpertacademy.com/main/code/problem/problemList.do

T = int(input())
for _ in range(1, T + 1):
    tc, N = input().split()
    lst = list(input().split())
    cnt_lst = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    num_word = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    for n in lst:
        for i in range(10):
            if n == num_word[i]:
                cnt_lst[i] += 1
                break
    answer = ''
    for i in range(10):
        answer += (num_word[i] + ' ') * cnt_lst[i]
    print(tc)
    print(answer)
