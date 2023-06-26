# 1208. Flatten
# Level D3
# Site: https://swexpertacademy.com/main/code/problem/problemList.do

for tc in range(1, 11):
    cnt = int(input())
    boxes = list(map(int, input().split()))
    for _ in range(cnt):
        max_idx = boxes.index(max(boxes))
        min_idx = boxes.index(min(boxes))
        boxes[max_idx] -= 1
        boxes[min_idx] += 1

    answer = max(boxes) - min(boxes)
    print(f'#{tc} {answer}')
