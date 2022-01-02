n = int(input())
dragon_curve = [list(map(int,input().split())) for _ in range(n)]

flying = [[0]*101 for _ in range(101)]
dx = [1,0,-1,0]
dy = [0,-1,0,1]
for i in range(len(dragon_curve)) :
    gen = 0
    x, y = dragon_curve[i][0], dragon_curve[i][1]
    flying[y][x] = 1
    turn = [dragon_curve[i][2]]

    while gen < dragon_curve[i][3] : # generation 커지면 stop
        for j in range(len(turn)-1,-1,-1) : # 방향 # 여기서 문제..! turn에 자꾸 추가 해줘서 문제생김.. 따로따로 만들까,,그냥

            rx = x + dx[turn[j]]
            ry = y + dy[turn[j]]

            flying[ry][rx] = 1
            turn.append((turn[j]+1) % 4)
            # print(turn)
            x = rx
            y = ry
            # for k in range(len(flying)):
            #     print(*flying[k])
            # turn += tmp

        gen += 1
cnt = 0
for k in range(0,101) :
    for l in range(0,101) :
        if flying[k][l] == 1 :
            if flying[k+1][l] == 1 and flying[k][l+1] == 1 and flying[k+1][l+1] == 1:
                cnt += 1
print(cnt)
