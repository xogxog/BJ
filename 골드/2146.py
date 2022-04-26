# 변수명 헷갈리는거 조심!!!
import sys
from collections import deque
input = sys.stdin.readline
# 상 우 하 좌
dr = [1,0,-1,0]
dc = [0,1,0,-1]

def land_chk() :
    global land_num
    while q :
        r,c = q.popleft()

        for i in range(4) :
            nr = r + dr[i]
            nc = c + dc[i]

            if 0<=nr<N and 0<=nc<N and island[nr][nc] and not visited[nr][nc] :
                q.append((nr,nc))
                visited[nr][nc] = 1
                my_island[nr][nc] = land_num


def bridge(_start) :
    global ans

    while q_2 :
        r,c = q_2.popleft()

        if ans <= visited[r][c] :
            pass
        else:
            for i in range(4) :
                nr = r+dr[i]
                nc = c+dc[i]
                if 0 > nr or nr>=N or 0>nc or nc>=N :
                    continue
                elif (not visited_2[nr][nc] or visited_2[nr][nc] > visited_2[r][c] + 1) and my_island[nr][nc] == 0 : # 바다인 경우
                    visited_2[nr][nc] = visited_2[r][c] + 1
                    q_2.append((nr,nc))
                elif my_island[nr][nc] != 0 and my_island[nr][nc] != _start : # 다른섬에 도착한 경우
                    # print(r,c,bridge_len)
                    if ans > visited_2[r][c] :
                        ans = visited_2[r][c]



N = int(input())
island = [list(map(int,input().split())) for _ in range(N)]
my_island = [[0]*N for _ in range(N)]
visited = [[0]*N for _ in range(N)]
land_num = 1
q = deque()
for i in range(N):
    for j in range(N):
        if island[i][j] == 1 and not visited[i][j] :
            q.append((i,j))
            visited[i][j] = 1
            my_island[i][j] = land_num
            land_chk()
            land_num += 1

ans = 987654321

visited_2 = [[0]*N for _ in range(N)]
q_2 = deque()
for k in range(N) :
    for l in range(N) :
        if my_island[k][l] : # 땅인 경우

            for m in range(4) :
                nr_2 = k + dr[m]
                nc_2 = l + dc[m]
                if 0<=nr_2<N and 0<=nc_2<N and my_island[nr_2][nc_2] == 0 and ( not visited_2[nr_2][nc_2] or visited_2[nr_2][nc_2] > 1 ): # 움직였을때 바다인 경우
                    q_2.append((nr_2,nc_2))
                    visited_2[nr_2][nc_2] = 1
                    bridge(my_island[k][l])
print(ans)