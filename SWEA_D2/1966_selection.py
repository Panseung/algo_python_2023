# 1966. 숫자를 정렬하자
# Level D2
# Site: https://swexpertacademy.com/main/code/problem/problemList.do
# 선택 정렬

def my_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[min_index] > arr[j]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    lst = list(map(int, input().split()))
    answer = my_sort(lst)
    print(f'#{tc}', end=' ')
    print(*answer)

    