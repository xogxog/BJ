from collections import deque
N,M = map(int,input().split()) # (r,c)
grim = [list(map(int,input().split())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]
dr = [0,0,1,-1]
dc = [-1,1,0,0]
num_grim = 0
ans = 0
for i in range(N) :
    for j in range(M):
        if grim[i][j] and not visited[i][j] :
            num_grim += 1
            q = deque()
            q.append((i,j))
            tmp_tot = 1
            visited[i][j] = 1

            while q :
                r,c = q.popleft()
                for k in range(4) :
                    nr = r+dr[k]
                    nc = c+dc[k]
                    if 0<=nr<N and 0<=nc<M and not visited[nr][nc] and grim[nr][nc] :
                        q.append((nr,nc))
                        visited[nr][nc] = 1
                        tmp_tot += 1

            ans = max(ans,tmp_tot)

print(num_grim)
print(ans)