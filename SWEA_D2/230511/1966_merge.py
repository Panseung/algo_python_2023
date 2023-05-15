# 1966. 숫자를 정렬하자
# Level D2
# Site: https://swexpertacademy.com/main/code/problem/problemList.do
# 병합 정렬

def my_sort(arr):
    if len(arr) < 2:
        return arr

    mid = len(arr) // 2
    left = my_sort(arr[:mid])
    right = my_sort(arr[mid:])

    merged_arr = []
    l = r = 0
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            merged_arr.append(left[l])
            l += 1
        else:
            merged_arr.append(right[r])
            r += 1

    merged_arr += left[l:]
    merged_arr += right[r:]
    return merged_arr


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    lst = list(map(int, input().split()))
    answer = my_sort(lst)
    print(f'#{tc}', end=' ')
    print(*answer)

