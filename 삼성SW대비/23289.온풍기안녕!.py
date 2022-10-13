import sys
from copy import deepcopy
from collections import deque
input = sys.stdin.readline
drc = [(0,1),(1,0)]

def move_r(room,r,c) : # 오른쪽으로 불어유~
    visited = [[0]*M for _ in range(N)]
    room[r][c+1] += 5 #가장 첫칸은 존재 and 벽 X
    visited[r][c+1] = 1
    q = deque()
    q.append((r,c+1,5))

    while q :
        rr,cc,wind = q.popleft()
        if wind == 1 :
            continue
        if 0<=rr<N and 0<=cc+1<M and not visited[rr][cc+1]and (rr,cc,rr,cc+1) not in wall_info : # 오른쪽에 벽X
            room[rr][cc+1] += wind-1
            visited[rr][cc+1] = 1
            q.append((rr,cc+1,wind-1))
        if 0<=rr-1<N and 0<=cc+1<M and not visited[rr-1][cc+1] and (rr,cc,rr-1,cc) not in wall_info and (rr-1,cc,rr-1,cc+1) not in wall_info : # 대각위
            room[rr-1][cc+1] += wind-1
            visited[rr-1][cc+1] = 1
            q.append((rr-1,cc+1,wind-1))
        if 0<=rr+1<N and 0<=cc+1<M and not visited[rr+1][cc+1] and (rr,cc,rr+1,cc) not in wall_info and (rr+1,cc,rr+1,cc+1) not in wall_info : # 대각아래
            room[rr+1][cc+1] += wind-1
            visited[rr+1][cc+1] = 1
            q.append((rr+1,cc+1,wind-1))

    return room
def move_l(room,r,c) : # 왼쪽으로 불어유~
    visited = [[0]*M for _ in range(N)]
    room[r][c-1] += 5 #가장 첫칸은 존재 and 벽 X
    visited[r][c-1] = 1
    q = deque()
    q.append((r,c-1,5))

    while q :
        rr,cc,wind = q.popleft()
        if wind == 1 :
            continue
        if 0<=rr<N and 0<=cc-1<M and not visited[rr][cc-1]and (rr,cc,rr,cc-1) not in wall_info : # 왼쪽벽체크
            room[rr][cc-1] += wind-1
            visited[rr][cc-1] = 1
            q.append((rr,cc-1,wind-1))
        if 0<=rr-1<N and 0<=cc-1<M and not visited[rr-1][cc-1] and (rr,cc,rr-1,cc) not in wall_info and (rr-1,cc,rr-1,cc-1) not in wall_info : # 대각왼위
            room[rr-1][cc-1] += wind-1
            visited[rr-1][cc-1] = 1
            q.append((rr-1,cc-1,wind-1))
        if 0<=rr+1<N and 0<=cc-1<M and not visited[rr+1][cc-1] and (rr,cc,rr+1,cc) not in wall_info and (rr+1,cc,rr+1,cc-1) not in wall_info : # 대각아래
            room[rr+1][cc-1] += wind-1
            visited[rr+1][cc-1] = 1
            q.append((rr+1,cc-1,wind-1))

    return room
def move_u(room, r, c):  # 위쪽으로 불어유~
    visited = [[0] * M for _ in range(N)]
    room[r-1][c] += 5  # 가장 첫칸은 존재 and 벽 X
    visited[r-1][c] = 1
    q = deque()
    q.append((r-1, c, 5))

    while q:
        rr, cc, wind = q.popleft()
        if wind == 1:
            continue
        if 0 <= rr-1 < N and 0 <= cc< M and not visited[rr-1][cc] and (rr, cc, rr-1, cc) not in wall_info:  # 위쪽벽쳌
            room[rr-1][cc] += wind - 1
            visited[rr-1][cc] = 1
            q.append((rr-1, cc, wind - 1))
        if 0 <= rr - 1 < N and 0 <= cc - 1 < M and not visited[rr - 1][cc - 1] and (rr, cc, rr, cc-1) not in wall_info and (rr, cc-1, rr-1, cc-1) not in wall_info:  # 대각왼위
            room[rr - 1][cc - 1] += wind - 1
            visited[rr - 1][cc - 1] = 1
            q.append((rr - 1, cc - 1, wind - 1))
        if 0 <= rr - 1 < N and 0 <= cc + 1 < M and not visited[rr - 1][cc + 1] and (rr, cc, rr, cc+1) not in wall_info and (rr, cc+1, rr-1, cc+1) not in wall_info:  #대각오른위
            room[rr - 1][cc + 1] += wind - 1
            visited[rr - 1][cc + 1] = 1
            q.append((rr - 1, cc + 1, wind - 1))

    return room
def move_d(room, r, c):  # 아래쪽으로 불어유~
    visited = [[0] * M for _ in range(N)]
    room[r+1][c] += 5  # 가장 첫칸은 존재 and 벽 X
    visited[r+1][c] = 1
    q = deque()
    q.append((r+1, c, 5))

    while q:
        rr, cc, wind = q.popleft()
        if wind == 1:
            continue
        if 0 <= rr+1 < N and 0 <= cc< M and not visited[rr+1][cc] and (rr, cc, rr+1, cc) not in wall_info:  # 아래쪽벽쳌
            room[rr+1][cc] += wind - 1
            visited[rr+1][cc] = 1
            q.append((rr+1, cc, wind - 1))
        if 0 <= rr + 1 < N and 0 <= cc - 1 < M and not visited[rr + 1][cc - 1] and (rr, cc, rr, cc-1) not in wall_info and (rr, cc-1, rr+1, cc-1) not in wall_info:  # 대각왼아래
            room[rr + 1][cc - 1] += wind - 1
            visited[rr + 1][cc - 1] = 1
            q.append((rr + 1, cc - 1, wind - 1))
        if 0 <= rr + 1 < N and 0 <= cc + 1 < M and not visited[rr + 1][cc + 1] and (rr, cc, rr, cc+1) not in wall_info and (rr, cc+1, rr+1, cc+1) not in wall_info:  #대각오른아래
            room[rr + 1][cc + 1] += wind - 1
            visited[rr + 1][cc + 1] = 1
            q.append((rr + 1, cc + 1, wind - 1))
    return room

def mix_air(room):
    tmp = [[0]*M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            for dr,dc in drc :
                nr = i+dr
                nc = j+dc
                if 0<=nr<N and 0<=nc<M and (i,j,nr,nc) not in wall_info :
                    air_temp = abs(room[nr][nc] - room[i][j]) // 4
                    if room[i][j] < room[nr][nc] :
                        tmp[i][j] += air_temp
                        tmp[nr][nc] -= air_temp
                    elif room[i][j] > room[nr][nc] :
                        tmp[nr][nc] += air_temp
                        tmp[i][j] -= air_temp
    for i in range(N):
        for j in range(M):
            tmp[i][j] += room[i][j]
    return tmp
def heat_the_room(room,gusaga):
    while 1 :
        if gusaga > 100 :
            return 101
    # 온풍기 바람불기
        for i in range(len(heater)): # deepcopy할 이유가 있을까?
            if heater[i][2] == 1 : # 방향 오른쪽
               tmp = move_r(room, heater[i][0],heater[i][1])
            elif heater[i][2] == 2 : # 왼쪽
                tmp = move_l(room,heater[i][0],heater[i][1])
            elif heater[i][2] == 3 : # 위
                tmp = move_u(room,heater[i][0],heater[i][1])
            else : # 아래
                tmp = move_d(room,heater[i][0],heater[i][1])

        room = mix_air(room)
        #가장 바깥쪽 온도 감소
        for r,c in lose_temp:
            if room[r][c] :
                room[r][c] -= 1
        #초콜렛 먹기
        gusaga += 1
        # 조사
        for r,c in check :
            if room[r][c] < K :
                break
        else :
            return gusaga # K이상이므로 종료



N,M,K = map(int,(input().split()))
grid = [list(map(int,input().split())) for _ in range(N)]
heater = []
check = []
ans = 0
for i in range(N):
    for j in range(M):
        if 0<grid[i][j]<=4 :
            heater.append((i,j,grid[i][j])) # 히터위치, 방향
        elif grid[i][j] == 5 :
            check.append((i,j)) # 온도 조사

W = int(input())
wall_info = set()
for _ in range(W):
    x,y,t = map(int,input().split())
    if t == 1 : # 1인 경우에는 (x, y)와 (x, y+1) 사이에 벽
        wall_info.add((x-1,y-1,x-1,y))
        wall_info.add((x-1,y,x-1,y-1))
    else : # 0인 경우 (x, y)와 (x-1, y) 사이에 벽 / x,y위치로부터 위아래 벽 체크하기쉽게하기위해
        wall_info.add((x-1,y-1,x-2,y-1))
        wall_info.add((x-2,y-1,x-1,y-1))
lose_temp = []
for i in range(N):
    for j in range(M):
        if i == 0 or i == N-1 :
            lose_temp.append((i,j))
        else :
            if j==0 or j==M-1:
                lose_temp.append((i,j))

print(heat_the_room([[0]*M for _ in range(N)],0))