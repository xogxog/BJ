import copy
import sys
from collections import deque
dr = [1,0,-1,0]
dc = [0,1,0,-1]


def bfs(lab) :
    global max_zero

    for i in range(n):
        for j in range(m):
            if lab[i][j] == 2:
                q.append([i,j])
    while q :
        r,c = q.popleft()

        for i in range(4):
            nr = r+dr[i]
            nc = c+dc[i]
            if 0<=nr<n and 0<=nc<m and lab[nr][nc] == 0 :
                lab[nr][nc] = 2
                q.append([nr,nc])

    cnt = 0
    for i in lab:
        cnt += i.count(0)
    max_zero = max(max_zero, cnt)


def wall(w) :
    if w == 3 :
        tmp_lab = copy.deepcopy(lab)
        bfs(tmp_lab)
        return

    for i in range(n):
        for j in range(m):
            if lab[i][j] == 0 :
                lab[i][j] = 1
                wall(w+1)
                lab[i][j] = 0


n,m = map(int,sys.stdin.readline().split())
lab = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
q = deque()

max_zero = 0
wall(0)
print(max_zero)