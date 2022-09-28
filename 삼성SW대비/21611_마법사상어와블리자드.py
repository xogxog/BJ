# 빙글빙글을 1차원 리스트로 펴서, 1차원 리스트에 상어위치부터 (0,0)까지 도는 순서 좌표를 넣어서
# 일일히 돌리지 않고 1차원 리스트를 그냥 for문돌려서 좌표 참고하는게 쉬울듯 -> 곤듀 지훈픽

import queue
import sys
from collections import deque
input = sys.stdin.readline

dirc = [(), (-1, 0), (1, 0), (0, -1), (0, 1)]
drc = [(0, -1), (1, 0), (0, 1), (-1, 0)]  # 좌하우상
N, M = map(int, input().split())


def group_pearl():

    move = 1
    max_move = N
    idx = 0  # 방향
    r, c = N//2, N//2
    bomb_flag = 0
    ls = []
    while 1:

        for _ in range(move):
            nr = r + drc[idx][0]
            nc = c + drc[idx][1]

            if A[r][c] == 0:  # 비어있는 공간
                pass
            elif A[r][c] == A[nr][nc]:
                ls.append((r, c))
            elif ls and A[r][c] != A[nr][nc]:
                ls.append((r, c))
                if len(ls) >= 4:
                    ans[A[r][c]] += len(ls)  # 폭발한 구슬 갯수 카운트
                    bomb_flag = 1
                    for i in range(len(ls)):
                        A[ls[i][0]][ls[i][1]] = 0
                ls = []
            r, c = nr, nc

            if r == 0 and c == 0:  # 종료 조건
                if bomb_flag:
                    return True
                else:
                    return False

        if idx % 2:
            move = min(max_move, move+1)

        idx = (idx+1) % 4


def fill_pearl():
    move = 1
    max_move = N
    idx = 0  # 방향
    r, c = N//2, N//2
    emp_q = deque()
    curr_num = 0
    while 1:

        for _ in range(move):
            nr = r + drc[idx][0]
            nc = c + drc[idx][1]

            if A[nr][nc] == 0:  # 비어있는 공간
                emp_q.append((nr, nc))
            elif A[nr][nc] != 0 and emp_q:  # 비어있는 공간 채울 수 있는 조건
                tmp_r, tmp_c = emp_q.popleft()
                A[tmp_r][tmp_c], A[nr][nc] = A[nr][nc], 0
                emp_q.append((nr, nc))

            r, c = nr, nc

            if r == 0 and c == 0:  # 종료 조건
                return

        if idx % 2:
            move = min(max_move, move+1)

        idx = (idx+1) % 4


def change_pearl():
    move = 1
    max_move = N
    idx = 0  # 방향
    r, c = N//2, N//2
    ls = []
    tmp = [0, 0]  # 구슬 개수, 구슬 번호
    while 1:

        for _ in range(move):
            nr = r + drc[idx][0]
            nc = c + drc[idx][1]

            if A[nr][nc] == 0:
                if tmp[0]:  # 매번 걸리는 조건문 이기도 함.
                    ls += tmp
                return ls
            elif not tmp[0] and A[nr][nc]:  # 구슬 없고, 숫자 있으면
                tmp[0] += 1
                tmp[1] = A[nr][nc]
            elif tmp[0] and tmp[1] == A[nr][nc]:  # 구슬 있고, 숫자 같으면
                tmp[0] += 1
            elif tmp[0] and tmp[1] != A[nr][nc]:  # 구슬 있고, 숫자 다르면
                ls += tmp
                tmp[0] = 1
                tmp[1] = A[nr][nc]

            r, c = nr, nc

            if r == 0 and c == 0:  # 종료 조건
                return

        if idx % 2:
            move = min(max_move, move+1)

        idx = (idx+1) % 4


def new_A(ls):
    tmp = [[0]*N for _ in range(N)]
    move = 1
    max_move = N
    idx = 0  # 방향
    r, c = N//2, N//2
    iidx = 0
    while iidx < len(ls):
        for _ in range(move):
            nr = r + drc[idx][0]
            nc = c + drc[idx][1]
            tmp[nr][nc] = ls[iidx]
            iidx += 1

            r, c = nr, nc

            if r == 0 and c == 0 or iidx >= len(ls):  # 종료 조건
                return tmp

        if idx % 2:
            move = min(max_move, move+1)
        idx = (idx+1) % 4

    return tmp


A = [list(map(int, input().split())) for _ in range(N)]
shark = N//2  # 상어위치
ans = [0, 0, 0, 0]
for _ in range(M):
    di, si = map(int, input().split())  # 방향, 거리

    # 파괴
    for i in range(1, si+1):
        A[shark + dirc[di][0] * i][shark + dirc[di][1] * i] = 0

    bomb = 1
    while bomb:
        fill_pearl()  # 구슬 빈칸 채우기
        bomb = group_pearl()  # 그룹별 터트리기

    ls = change_pearl()

    tmp_ls = new_A(ls)
    A = [l[:] for l in tmp_ls]


print(ans[1]+2*ans[2]+3*ans[3])
