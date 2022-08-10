import sys
from collections import deque
input = sys.stdin.readline

dr = [0,0,1,-1]
dc = [-1,1,0,0]

def cnt_cluster(i,j,idx) :
    q = deque()
    q.append((i,j))
    ls[i][j] = idx
    visited[i][j] = 1
    check = False # 땅에 닿아있는지 체크
    while q :
        r,c = q.popleft()
        for i in range(4) :
            nr = r + dr[i]
            nc = c + dc[i]
            if 0<=nr<R and 0<=nc<C and ls[nr][nc] != 0 and not visited[nr][nc] :
                visited[nr][nc] = 1
                q.append((nr,nc))
                ls[nr][nc] = idx
                if nr == R-1 :
                    check = True

    return check

def go_down(idx, ls) :
    
    tmp = [l[:] for l in ls]
    while 1 :
        for i in range(R-1,0,-1) :
            for j in range(C-1,-1,-1) :
                if ls[i-1][j] == idx and ls[i][j] == 0 : # 위에 클러스터 있고 현재 빈칸이면 내리기
                    ls[i][j] = idx
                    ls[i-1][j] = 0
                elif ls[i-1][j] == idx and ls[i][j] != 0 : # 클러스터 못내림
                    return tmp
        tmp = [l[:] for l in ls]
        # print(f'=======클러스터 내리는중==========')
        # for z in range(R):
        #     print(*ls[z])
        if ls[R-1][:].count(idx) != 0 :
            break

    return ls # 클러스터 내리기 완성


def war() :
    global tmp_ls, idx, visited, ls

    for k in range(N):
        if k % 2 == 0:  # 짝수이면 왼쪽에서 던짐
            for l in range(C):
                if ls[R- throw[k]][l] != 0:
                    ls[R - throw[k]][l] = 0
                    break
        else:  # 오른쪽에서 던짐
            for m in range(C - 1, -1, -1):
                if ls[R - throw[k]][m] != 0:
                    ls[R - throw[k]][m] = 0
                    break
        # print(f'=======던짐==========')
        #         # for z in range(R):
        #         #     print(*ls[z])
        #         # tmp_ls = [lss[:] for lss in ls]

        # 클러스터 재정의
        visited = [[0] * C for _ in range(R)]
        on_ground = [] # 땅에 붙어있는 미네랄 체크
        for i in range(R):
            for j in range(C):
                if ls[i][j] != 0 and not visited[i][j]:
                    idx += 1
                    check = cnt_cluster(i, j, idx)
                    if not check :
                        on_ground.append(idx)

        # tmp_ls = [lss[:] for lss in ls]
        # print(f'===== 클러스터 재정의 ============')
        # for z in range(R):
        #     print(*ls[z])

        # 땅에 붙어있지 않은 클러스터 밑으로 내려보내기
        for n in range(len(on_ground)) :
            ls = go_down(on_ground[n],ls)

        # print(f'=================')
        # for z in range(R) :
        #     print(*ls[z])



R,C = map(int,input().split())
ls = [input().rstrip() for _ in range(R)]
N = int(input()) # 막대던진횟수
throw = list(map(int,input().split())) # 짝수 : 왼쪽, 홀수 : 오른쪽
cluster = 0 # 클러스터 갯수

idx = 0
tmp_ls = [[0]*C for _ in range(R)]
visited = [[0]*C for _ in range(R)]

for i in range(R) :
    for j in range(C) :
        if ls[i][j] == 'x' and not visited[i][j] :
            idx += 1
            # cnt_cluster(i,j, idx)
            q = deque()
            q.append((i, j))
            tmp_ls[i][j] = idx
            visited[i][j] = 1
            while q:
                r, c = q.popleft()
                for k in range(4):
                    nr = r + dr[k]
                    nc = c + dc[k]
                    if 0 <= nr < R and 0 <= nc < C and ls[nr][nc] == 'x' and not visited[nr][nc]:
                        visited[nr][nc] = 1
                        q.append((nr, nc))
                        tmp_ls[nr][nc] = idx

ls = [tmp[:] for tmp in tmp_ls]

war()

for x in range(R) :
    for y in range(C) :
        if ls[x][y] == 0 :
            print('.', end='')
        else :
            print('x', end= '')
    print()