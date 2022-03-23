import sys
from collections import deque
input = sys.stdin.readline

drc = [[-1, 0], [1, 0], [0, -1], [0, 1]]

def bfs(r, c, destroy):
    global min_cnt

    q = deque()
    q.append((r, c, destroy))
    while q:
        cr, cc, destroy = q.popleft()
        if cr == n-1 and cc == m-1:
            break
        for i in range(4):
            mr = cr + drc[i][0]
            mc = cc + drc[i][1]
            if mr < 0 or mr >= n or mc < 0 or mc >= m: continue
            if visited[mr][mc] !=0 and visited[mr][mc] < visited[cr][cc] + 1: continue
            if maze[mr][mc] == '0':
                visited[mr][mc] = visited[cr][cc] + 1
                q.append((mr, mc, destroy))
            elif destroy == 0:
                visited[mr][mc] = visited[cr][cc] + 1
                q.append((mr, mc, 1))
    # print(f'=======================')
    # for j in range(n) :
    #     print(*visited[j])
n, m = map(int, input().split())
maze = [input().rstrip() for _ in range(n)]
# print(maze)
visited = [[0]*m for _ in range(n)]
visited[0][0] = 1

bfs(0, 0, 0)
if visited[n-1][m-1] == 10000 :
    print(-1)
else :
    print(visited[n-1][m-1])