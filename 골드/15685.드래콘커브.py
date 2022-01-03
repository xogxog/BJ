n = int(input())
dragon_curve = [list(map(int,input().split())) for _ in range(n)]

flying = [[0]*101 for _ in range(101)]
# 우, 상, 좌, 하 # r : 행 , c : 열
dc = [1,0,-1,0]
dr = [0,-1,0,1]
for i in range(len(dragon_curve)) :
    gen = 0
    c, r = dragon_curve[i][0], dragon_curve[i][1]
    flying[r][c] = 1
    turn = [dragon_curve[i][2]]

    # turn 할 방향 세대수 만큼 배열에 넣어주기
    while gen < dragon_curve[i][3] : # generation 커지면 stop
        for j in range(len(turn)-1,-1,-1) :
            turn.append((turn[j]+1) % 4)
        gen += 1

    for t in turn :
        nr = r + dr[t]
        nc = c + dc[t]

        flying[nr][nc] = 1

        c = nc
        r = nr

cnt = 0
for k in range(0,100) :
    for l in range(0,100) :
        if flying[k][l] and flying[k+1][l] and flying[k][l+1] and flying[k+1][l+1] :
            cnt += 1
print(cnt)
