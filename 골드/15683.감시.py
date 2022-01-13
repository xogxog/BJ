from collections import deque
from copy import deepcopy

def dfs(curr_cctv_num) :
    global visited, ans

    if curr_cctv_num == len(cctv) :
        tmp_ans = 0
        for l in range(N) :
            for m in range(M) :
                if room[l][m] ==0 and visited[l][m] == 0 :
                    tmp_ans += 1
        if tmp_ans < ans :
            # for z in range(N) :
            #     print(*visited[z])
            # print(f'===============')
            
            ans = tmp_ans
        return
    else :

            
        r,c = cctv[curr_cctv_num]
        q = deque()
        for j in direction[room[r][c]] :
            for k in j :
                nr = r + dr[k]
                nc = c + dc[k]

                while 0<=nr<N and 0<=nc<M and room[nr][nc] != 6 : # 옮기는 좌표가 범위안, 벽이 아니라면 계속 가야함
                    if room[nr][nc] == 0 : # 경로가 겹치는 경우엔 합쳐서 가야함 ,, ! cctv끼리는 뚫을 수 있음
                        visited[nr][nc] += 1
                        q.append((nr,nc))
                    nr = nr + dr[k]
                    nc = nc + dc[k]
            dfs(curr_cctv_num+1)
            # visited 전상태로 되돌려 주기 / 5의 한가지 경우의 수만 있으므로 냅둠

            while q : # visited 전 상태로 돌려주기
                x, y = q.popleft()
                visited[x][y] -= 1
                # for o in range(len(q)) :
                #     x,y = q[o]
                #     visited[x][y] -= 1
                


N,M = map(int,input().split()) # 4 6 이면 세로 4 가로 6
room =[list(map(int,input().split())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]
ans = 987654321
direction = [
    [],
    [[0],[1],[2],[3]], # 1번 cctv
    [[0,2],[1,3]], # 2번 cctv
    [[0,3],[0,1],[1,2],[2,3]], # 3번 cctv
    [[0,2,3],[0,1,3],[0,1,2],[1,2,3]], # 4번 cctv
    [[0,1,2,3]] # 5번 cctv
]

# 우 하 좌 상
dr = [0,1,0,-1]
dc = [1,0,-1,0]

cctv = [] # cctv 갯수

# cctv 갯수 알기
for r in range(N) :
    for c in range(M) :
        if room[r][c] in {1,2,3,4} : # set 이 빠르다. - 공주 왈
            cctv.append((r,c))
        if room[r][c] == 5 :
            for p in range(4) :
                tmp_nr = r + dr[p]
                tmp_nc = c + dc[p]

                while 0<=tmp_nr<N and 0<=tmp_nc<M and room[tmp_nr][tmp_nc] != 6 : 
                        if room[tmp_nr][tmp_nc] == 0 : 
                            visited[tmp_nr][tmp_nc] = 1
                        tmp_nr = tmp_nr + dr[p]
                        tmp_nc = tmp_nc + dc[p]
dfs(0) # cctv 갯수 만큼 보도록
print(ans)

