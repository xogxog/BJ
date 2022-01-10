def cleaning(x,y,up_or_down) :

    tmp = 0  # 그 전 값 담아둘 변수
    flag = 0
    for k in range(4):
        if up_or_down == "down" and k % 2:  # 아래 공기청정기이고, 홀 일때는 반대 방향
            nx = x - dr[k]
            ny = y - dc[k]

        else :
            nx = x + dr[k]
            ny = y + dc[k]
        while 0 <= nx < R and 0 <= ny < C:  # 움직일 범위 안에 있을 때 까지만 돌기

            if dust[nx][ny] == -1:  # 다 돌아서 공기청정기랑 만났을 때, 종료
                flag = 1
                break

            if dust[x][y] == -1: # 시작
                tmp = dust[nx][ny]
                dust[nx][ny] = 0
            else:
                tmp, dust[nx][ny] = dust[nx][ny], tmp

            x, y = nx, ny

            if up_or_down == "down" and k % 2:  # 아래 공기청정기이고, 홀 일때는 반대 방향
                nx = x - dr[k]
                ny = y - dc[k]

            else:
                nx = x + dr[k]
                ny = y + dc[k]

            # for z in range(R):
            #     print(*dust[z])
            # print(f'==========================')
            # print(nx, ny)
        if flag :
            break


R, C, T = map(int, input().split())  # 행, 열, 초

dust = [list(map(int, input().split())) for _ in range(R)]
cleaner = []
# 공기청정기 위치
for n in range(R):
    for o in range(C):
        if dust[n][o] == -1:
            cleaner.append([n, o])
            cleaner.append([n+1, o])
    if len(cleaner):
        break
time = 0

# 우 상 좌 하
dr = [0, -1, 0, 1]
dc = [1, 0, -1, 0]


while time < T:
    tmp_dust = [[0]*C for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if dust[i][j] != 0 and dust[i][j] != -1:  # 먼지가 있는 곳
                check = 0  # 먼지 몇칸 퍼졌는지 체크
                for k in range(4):  # 먼지 퍼뜨리기
                    nr = i + dr[k]
                    nc = j + dc[k]

                    # 범위내에 있고, 공기청정기가 없는곳이면
                    if 0 <= nr < R and 0 <= nc < C and dust[nr][nc] != -1:
                        tmp_dust[nr][nc] += dust[i][j] // 5
                        check += 1
                dust[i][j] = dust[i][j] - ((dust[i][j]//5) * check)

    # 먼지 임시로 저장해둔 것 합치기
    for l in range(R):
        for m in range(C):
            dust[l][m] += tmp_dust[l][m]
    turn_dust = [[0]*C for _ in range(R)]
    # 공기청정기로 회전
    cleaning(cleaner[0][0], cleaner[0][1], 'up')
    cleaning(cleaner[1][0],cleaner[1][1],'down')

    time += 1
ans = 0
for e in range(R) :
    ans += sum(dust[e])
print(ans +2)



