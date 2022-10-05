import sys
from collections import deque
input = sys.stdin.readline

drc = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 우하좌상 순서


def bfs():
    q = deque()
    # {[(0,0,0)]} -> 이런 튜플을 가진 리스트를 set으로 변환하겠다. / set((0,0,0)) -> 결과 : {0}
    visited = {(0, 0, 0)}
    q.append((0, 0, 0, 1))  # r,c,destroy,cnt
    while q:

        r, c, destroy, cnt = q.popleft()
        if r == n-1 and c == m-1:
            return cnt
        for i in range(4):
            # for dr,dc in drc :
            nr = r + drc[i][0]
            nc = c + drc[i][1]

            if 0 <= nr < n and 0 <= nc < m and (nr, nc, destroy) not in visited:
                if maze[nr][nc] == '0':  # 길
                    q.append((nr, nc, destroy, cnt+1))
                    visited.add((nr, nc, destroy))
                elif maze[nr][nc] == '1' and destroy == 0:
                    q.append((nr, nc, 1, cnt+1))
                    visited.add((nr, nc, 1))
    return -1


n, m = map(int, input().split())
maze = [input().rstrip() for _ in range(n)]


print(bfs())
