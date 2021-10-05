# 2178. 미로 탐색
import sys
from collections import deque

dr = [0,0,1,-1]
dc = [1,-1,0,0]

def bfs() :
    while q :
        r, c = q.popleft()

        if r == N-1 and c == M-1 :
            return

        for i in range(4) :
            mr = r + dr[i]
            mc = c + dc[i]

            if 0<=mr<N and 0<=mc<M and ls[mr][mc] == 1 :
                q.append((mr,mc))
                ls[mr][mc] = 1 + ls[r][c]





N,M = map(int,sys.stdin.readline().split()) # 4 * 6
ls = [list(map(int,sys.stdin.readline().rstrip())) for _ in range(N)]
# print(ls)

q = deque()
q.append((0,0))
bfs()

print(ls[N-1][M-1])