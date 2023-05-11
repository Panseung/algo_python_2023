# 1966. 숫자를 정렬하자
# Level D2
# Site: https://swexpertacademy.com/main/code/problem/problemList.do
# 버블 정렬

def my_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    lst = list(map(int, input().split()))
    answer = my_sort(lst)
    print(f'#{tc}', end=' ')
    print(*answer)
