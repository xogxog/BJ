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
print(cleaner)

time = 0

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
    for  in range(5) :
        x , y =


    time += 1
