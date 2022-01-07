from collections import deque
gear = list(deque(map(int,input())) for _ in range(4))
turn = int(input())

for _ in range(turn) :
    n, d = map(int,input().split()) #톱니바퀴, 방향(1 시계방향, -1 반시계방향)
    p = [0, 0, 0, 0]  # 돌릴 방향
    if n == 1:
        p[0] = d
        if gear[0][2] != gear[1][6] :
            p[1] = p[0] * -1
            if gear[1][2] != gear[2][6] :
                p[2] = p[1] * -1
                if gear[2][2] != gear[3][6] :
                    p[3] = p[2] * -1
    elif n == 2 :
        p[1] = d
        if gear[1][6] != gear[0][2] :
            p[0] = p[1] * -1
        if gear[1][2] != gear[2][6] :
            p[2] = p[1] * -1
            if gear[2][2] != gear[3][6]:
                p[3] = p[2] * -1
    elif n == 3 :
        p[2] = d
        if gear[2][2] != gear[3][6] :
            p[3] = p[2] * -1
        if gear[2][6] != gear[1][2] :
            p[1] = p[2] * -1
            if gear[1][6] != gear[0][2] :
                p[0] = p[1] * -1
    else :
        p[3] = d
        if gear[3][6] != gear[2][2] :
            p[2] = p[3]*-1
            if gear[2][6] != gear[1][2] :
                p[1] = p[2]*-1
                if gear[1][6] != gear[0][2] :
                    p[0] = p[1]*-1

    for i in range(4) :
        if p[i] == -1 :
            # tmp = gear[i].popleft()
            # gear[i].append(tmp)
            # deque 속성에 rotate가 있다 !
            gear[i].rotate(p[i])
        elif p[i] == 1 :
            # tmp = gear[i].pop()
            # gear[i].appendleft(tmp)
            gear[i].rotate(p[i])

ans = 0
for j in range(4) :
    if gear[j][0] == 1 :
        ans += (2**j)
print(ans)