import sys
from collections import deque
input = sys.stdin.readline

dr = [0,0,1,-1]
dc = [1,-1,0,0]

def red_green_diff(ii,jj,color) :
    q = deque()
    q.append((ii,jj))
    while q :
        r,c = q.popleft()
        for i in range(4):
            nr = r+dr[i]
            nc = c+dc[i]
            if 0<=nr<N and 0<=nc<N and not visited[nr][nc] and ground[nr][nc] == color :
                visited[nr][nc] = 1
                q.append([nr,nc])


def red_green_same(ii,jj,color) :
    q = deque()
    q.append((ii,jj))
    while q :
        r,c = q.popleft()
        for i in range(4):
            nr = r+dr[i]
            nc = c+dc[i]
            if color == 'R' or color == 'G' :
                if 0<=nr<N and 0<=nc<N and not visited2[nr][nc] and (ground[nr][nc]=='R' or ground[nr][nc]=='G'):
                    visited2[nr][nc]=1
                    q.append((nr,nc))
            else :
                if 0<=nr<N and 0<=nc<N and not visited2[nr][nc] and ground[nr][nc]=='B':
                    visited2[nr][nc]=1
                    q.append((nr,nc))


N = int(input())

ground = [list(input()) for _ in range(N)]
visited = [[0]*N for _ in range(N)]
visited2 = [[0]*N for _ in range(N)]
cnt = 0
cnt2 = 0
for i in range(N) :
    for j in range(N):
        if not visited[i][j] :
            visited[i][j] = 1
            cnt += 1
            red_green_diff(i,j,ground[i][j])
        if not visited2[i][j] :
            visited2[i][j] = 1
            cnt2 += 1
            red_green_same(i,j,ground[i][j])
print(cnt, cnt2)