from collections import deque

dr = [0,0,1,-1]
dc = [1,-1,0,0]

def bfs(j,k) :
    visited[j][k] = 1
    q = deque([(j,k)])

    while q :

        r, c = q.popleft()

        for m in range(4) :

            nr = r + dr[m]
            nc = c + dc[m]

            if 0<=nr<N and 0<=nc<M and not visited[nr][nc] and farm[nr][nc] :
                q.append((nr,nc))
                visited[nr][nc] = 1




for _ in range(int(input())):
    M, N, K = map(int, input().split())

    farm = [[0] * M for _ in range(N)]
    visited = [[0] * M for _ in range(N)]
    for i in range(K):
        x, y = map(int, input().split())
        farm[y][x] = 1
    ans = 0
    for j in range(N) :
        for k in range(M) :
            if not visited[j][k] and farm[j][k] == 1:
                bfs(j,k)
                ans += 1
    print(ans)