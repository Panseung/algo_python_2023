# 1493. 수의 새로운 연산
# Level D3
# Site: https://swexpertacademy.com/main/code/problem/problemList.do

def find_pos(num):
    x, y = 1, 1

    v = 1
    while v < num:
        x += 1
        y -= 1
        v += 1
        if y == 0:
            y = x
            x = 1

    return x, y


def find_num(pos_x, pos_y):
    res_x, res_y = 1, 1
    answer = 1
    while pos_x != res_x or pos_y != res_y:
        res_x += 1
        res_y -= 1
        answer += 1
        if res_y == 0:
            res_y = res_x
            res_x = 1

    return answer


T = int(input())
for tc in range(1, T + 1):
    p, q = map(int, input().split())
    px, py = find_pos(p)
    qx, qy = find_pos(q)
    new_x, new_y = px + qx, py + qy
    result = find_num(new_x, new_y)

    print(f'#{tc} {result}')
