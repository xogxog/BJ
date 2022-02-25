# 탈옥
# 탈옥하게 해줘,,,,
import sys
from collections import deque

# 하 상 우 좌
dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

for _ in range(int(input())):
    h, w = map(int, input().split())
    prison = [list(sys.stdin.readline().strip()) for _ in range(h)]
    visited = [[0]*w for _ in range(h)]
    q = deque()

    # 탈옥수 위치 찾기
    for i in range(h):
        for j in range(w):
            if prison[h][w] == '$':
                q.append((i, j))  # 탈옥수

                while q:
                    r, c = q.popleft()

                    for k in range(4) :

                        nr = r + dr[k]
                        nc = c + dc[k]

                        if 0<=nr<h and 0<=nc<w
