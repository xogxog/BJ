import sys
from collections import deque

dr = [1,-1,0,0]
dc = [0,0,1,-1]

input = sys.stdin.readline

M,N = map(int,input().split()) # 가로, 세로
tomato = [list(map(int,input().split())) for _ in range(N)]

cnt = 0
for i in range(N):
    cnt += tomato[i].count(1)
if cnt == M *N :
    print(0)
else :
    day = 0
    q = deque()
    for i in range(N) :
        for j in range(M) :
            if tomato[i][j] == 1:
                q.append((i,j,day))

    while q :

        r, c ,day= q.popleft()

        for k in range(4) :
            nr = r + dr[k]
            nc = c + dc[k]
            if 0>nr or nr>=N or 0>nc or nc>=M :
                continue
            elif tomato[nr][nc] == 0 :
                tomato[nr][nc] = 1
                q.append((nr,nc,day+1))

    for l in range(N) :
        if tomato[l].count(0) :
            print(-1)
            break
    else :
        print(day)