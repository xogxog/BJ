# 7562 . 나이트의 이동
# bfs
import sys
from collections import deque
# 나이트가 이동 할 수 있는 경우의 수
dr = [-2, -2, -1, 1, 2, 2, 1, -1]
dc = [-1, 1, 2, 2, -1, 1, -2, -2]

# 시간 초과(dfs)
# def move_night(r,c, cnt) :
#     global to_r, to_c, min_cnt
#     if r == to_r and c == to_c :
#         if min_cnt > cnt :
#             min_cnt = cnt
#             return
#
#     if cnt >= min_cnt :
#         return
#
#     for i in range(8):
#         mr = r + dr[i]
#         mc = c + dc[i]
#
#         if 0<=mr<N and 0<=mc<N and not visited[mr][mc] :
#             visited[mr][mc] = 1
#             # for k in range(N) :
#             #     print(*visited[k])
#             # print(f'========================')
#             move_night(mr,mc, cnt+1)
#             visited[mr][mc] = 0


def move_night() :
    global to_r, to_c

    while q :
        r,c = q.popleft()

        for i in range(8):
            mr = r + dr[i]
            mc = c + dc[i]
            if r == to_r and c == to_c:
                return # bfs이므로 처음 도착하는게 최단 거리이다.
            if 0 <= mr < N and 0 <= mc < N and (visited[mr][mc] == 0 or 1+ visited[r][c]<visited[mr][mc] ) :
                visited[mr][mc] = 1+ visited[r][c]
                q.append([mr,mc])
                # for k in range(N) :
                #     print(*visited[k])
                # print(f'========================')



for _ in range(0, (int(sys.stdin.readline()))):
    N = int(sys.stdin.readline().rstrip())
    r , c = map(int, sys.stdin.readline().split())       # 말의 위치
    to_r , to_c = map(int, sys.stdin.readline().split()) # 이동할 곳

    visited = [[0]*N for _ in range(N)]
    # min_cnt = N*N
    # cnt = 0

    q = deque()
    q.append((r,c))
    # move_night(r,c, cnt)
    move_night()
    if r == to_r and c == to_c :
        print(0)
    else :
        print(visited[to_r][to_c])