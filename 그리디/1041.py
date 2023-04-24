# 1041. 주사위
# Level G5
# Link : https://www.acmicpc.net/problem/1041

import sys

input = sys.stdin.readline

N = int(input())
a, b, c, d, e, f = map(int, input().split())

one_view_cnt = max((N - 2) * (N - 2) * 5 + (N - 2) * 4, 0)
two_view_cnt = max((N - 2) * 8 + 4, 0)
three_view_cnt = 4

two_case = [a + b, a + c, a + d, a + e, b + c, b + d, b + f, c + e, c + f, d + e, d + f, e + f]
three_case = [a + b + c, a + b + d, a + c + e, a + d + e, b + c + f, b + d + f, c + e + f, d + e + f]

one_min = min(a, b, c, d, e, f)
two_min = min(two_case)
three_min = min(three_case)

answer = one_min * one_view_cnt + two_view_cnt * two_min + three_view_cnt * three_min
if N == 1:
    answer = a + b + c + d + e + f - max(a, b, c, d, e, f)
print(answer)
