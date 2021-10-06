# 2206 - 벽 부수고 이동하기

# 상하좌우
dr = [-1,1,0,0]
dc = [0,0,-1,1]

def dfs(r,c,road,crush):
    global ans
    if road > ans :
        ans = road

    visited[r][c] = 1

    for i in range(4) :
        nr = r + dr[i]
        nc = c + dc[i]

        if 0<=nr<N and 0<=nc<M and not visited[nr][nc] :















N,M = map(int,input().split())
ls = [input() for _ in range(N)]
visited = [[0] * M for _ in range(N)]
ans = 0

crush = 1
road = 1
dfs(0,0,road,crush)











