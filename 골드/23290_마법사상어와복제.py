import sys
import copy
from collections import deque
input = sys.stdin.readline

dr = [0,-1,-1,-1,0,1,1,1]
dc = [-1,-1,0,1,1,1,0,-1]

# 상좌하우
ddr = [-1,0,1,0]
ddc = [0,-1,0,1]

def shark_move(ls,fish_cnt ,move_cnt,visited) : # 상어 지나온길, 먹은 물고기 수, 움직임 수
    global max_fish, s_move_route

    if move_cnt == 3 :
        if max_fish < fish_cnt :
            max_fish = fish_cnt
            s_move_route = [l[:]for l in ls]
        return

    r = ls[-1][0]
    c = ls[-1][1]

    for i in range(4) :
        nr = r + ddr[i]
        nc = c + ddc [i]
        if 0<=nr<4 and 0<=nc<4 :
            if not visited[nr][nc] :
                visited[nr][nc] = 1
                ls.append((nr,nc))
                shark_move(ls,fish_cnt+len(move[nr][nc]),move_cnt+1,visited)
                visited[nr][nc] = 0
                ls.pop()
            else :
                ls.append((nr, nc))
                shark_move(ls, fish_cnt , move_cnt + 1, visited)
                ls.pop()



M,S = map(int,input().split())                      # 물고기 수, 마법 연습 횟수
ocean = [[[] for _ in range(4)] for i in range(4)]  # 물고기 지도
smell_cnt = [[0]*4 for _ in range(4)]                     # 물고기 냄새 cnt

for _ in range(M) :
    f1,f2,d = map(int,input().split())
    ocean[f1-1][f2-1].append(d-1)

sr,sc = map(int,input().split()) # 상어 위치
sr -= 1
sc -= 1
max_fish = -1
s_move_route = []
for _ii in range(S) :

    move = [[[] for _ in range(4)] for i in range(4)]
    for i in range(4):
        for j in range(4):
            for k in ocean[i][j]:

                nr = i + dr[k]
                nc = j + dc[k]
                cnt = 0
                while cnt < 8:
                    if 0 <= nr < 4 and 0 <= nc < 4 and (nr != sr or nc != sc) and not smell_cnt[nr][nc]:  # 2.조건 만족
                        move[nr][nc].append(k)  # move에 물고기 방향 넣기
                        break
                    else:
                        cnt += 1
                        k = (k - 1) % 8
                        nr = i + dr[k]
                        nc = j + dc[k]
                if cnt == 8:
                    move[i][j].append(k)  # 제자리 넣기

    # 3. 상어 -> 물고기 먹을 루트 구하기
    visited = [[0] * 4 for _ in range(4)]

    for l in range(4):
        _nr = sr + ddr[l]
        _nc = sc + ddc[l]
        if 0<=_nr<4 and 0<=_nc<4  :
            visited[_nr][_nc] = 1
            fish_cnt = len(move[_nr][_nc])
            ls = [(_nr, _nc)]
            shark_move(ls, fish_cnt, 1,visited)
            visited[_nr][_nc] = 0


    for nnr,nnc in s_move_route :
        if len(move[nnr][nnc]) :
            move[nnr][nnc] = [] # 다 잡아먹음
            smell_cnt[nnr][nnc] = 3 # 물고기 냄새

        # 상어 최종 위치 바꿔주기
        sr = nnr
        sc = nnc

    # 4. 물고기 냄새 지우기
    for n in range(4):
        for o in range(4):
            if smell_cnt[n][o]:
                smell_cnt[n][o] -= 1

    # 5. 물고기복사
    for p in range(4):
        for q in range(4):
            for t in move[p][q] :
                ocean[p][q].append(t)


    max_fish = -1
    s_move_route = []

ans = 0
for _k in range(4):
    for _l in range(4):
       ans += len(ocean[_k][_l])
print(ans)