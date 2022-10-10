# 틀린이유
# 승객과, 도착지의 위치를 한 리스트에 담아서 a승객의 도착지와 b승객의 출발지가 같은 경우 고려 X
# 각 승객의 출발지와 목적지는 다르다 != 각 승객의 목적지는 다르다
# 각 승객의 목적지가 같다는 것을 염두해 두고 문제를 풀어야 한다.
import sys
from collections import deque
input = sys.stdin.readline
drc = [(-1,0),(0,-1),(0,1),(1,0)]

N,M ,fuel = map(int,input().split())
grid = [list(map(int,input().split())) for _ in range(N)]
passengers = [[0]*N for _ in range(N)]
goal = {}
taxi = tuple(map(lambda x : x-1,map(int,(input()+' 1').split())))
flag = 0
p_idx = 1 # 승객 번호
for _ in range(M):
    p_r,p_c,g_r,g_c = map(int,input().split())
    passengers[p_r-1][p_c-1] = p_idx
    goal[p_idx] = (g_r-1,g_c-1)
    p_idx += 1

for _ in range(M):
    # 가장 가까이 있는 승객 파악
    near_passengers = []
    near_passenger = (0, 0, 0)
    nearest = 0
    if passengers[taxi[0]][taxi[1]]:  # 택시 위치 = 승객 위치
        near_passenger = taxi
    else:
        q = deque([taxi])
        visited = [[0] * N for i in range(N)]
        visited[taxi[0]][taxi[1]] = 1
        while q:
            r, c, d = q.popleft()
            if passengers[r][c] and not near_passengers:  # 첫 승객발견!
                nearest = d
                near_passengers.append((r, c, d))
            elif passengers[r][c] and near_passengers:  # 첫 승객 이후
                if nearest == d:
                    near_passengers.append((r, c, d))
                else:  # 첫 승객보다 머니까 break
                    break
            for dr, dc in drc:
                nr = r + dr
                nc = c + dc
                if 0 <= nr < N and 0 <= nc < N and not grid[nr][nc] and not visited[nr][nc]:
                    visited[nr][nc] = 1
                    q.append((nr, nc, d + 1))
        if len(near_passengers) == 0:  # 택시가 손님 못태우는 경우
            flag = 1
            break
        if len(near_passengers) == 1:
            near_passenger = near_passengers[0]
        else:
            near_passengers.sort(key=lambda x: (x[0], x[1]))  # 행,열 정렬 한번에
            near_passenger = near_passengers[0]

    # 승객 태우고 목적지로 이동!
    goal_rc = goal[passengers[near_passenger[0]][near_passenger[1]]] # 손님이 가야하는 목표지점의 좌표

    move_visited = [[0]*N for i in range(N)]
    move_visited[near_passenger[0]][near_passenger[1]] = 1 # 출발 지점

    move_q = deque()
    move_q.append((near_passenger[0],near_passenger[1],0))

    arrived = (-1,-1,-1)
    while move_q :
        r,c,d = move_q.popleft()
        if goal_rc == (r,c) : # 목적지 도착
            arrived = (r,c,d)
            break
        for dr,dc in drc :
            nr = r+dr
            nc = c+dc
            if 0<=nr<N and 0<=nc<N and not grid[nr][nc] and not move_visited[nr][nc] :
                move_visited[nr][nc] = 1
                move_q.append((nr,nc,d+1))
    if arrived == (-1,-1,-1) : # 도착지가는길이 가로막힌 경우
        flag = 1
        break
    # 연료 계산
    fuel -= (arrived[2] + near_passenger[2])
    if fuel <0 : # 도착 못함
        flag = 1
        break
    else :
        fuel += arrived[2]*2
        taxi = (arrived[0],arrived[1],0)
    passengers[near_passenger[0]][near_passenger[1]] = 0 # 손님 지도에서 지우기
if flag :
    print(-1)
else :
    print(fuel)