# 1052. 물병
# Level S1
# Link : https://www.acmicpc.net/problem/1052

import sys

input = sys.stdin.readline

n, k = map(int, input().split())
count = 0
while bin(n).count('1') > k:
    n += 1
    count += 1

print(count)
