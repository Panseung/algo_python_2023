# 1966. 숫자를 정렬하자
# Level D2
# Site: https://swexpertacademy.com/main/code/problem/problemList.do
# 퀵 정렬

def my_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left, right, equal = [], [], []
    for i in arr:
        if i < pivot:
            left.append(i)
        elif i > pivot:
            right.append(i)
        else:
            equal.append(i)
    return my_sort(left) + equal + my_sort(right)


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    lst = list(map(int, input().split()))
    answer = my_sort(lst)
    print(f'#{tc}', end=' ')
    print(*answer)
