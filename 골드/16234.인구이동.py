from collections import deque
def bfs() :
    global sub_total, ans, is_move, sub_lst
    cnt = 1

    while q :

        r, c = q.popleft()

        for i in range(4) :
            nr = r + dr[i]
            nc = c + dc[i]

            if 0<=nr<n and 0<=nc<n and not visited[nr][nc] and left <= abs(popular[r][c] - popular[nr][nc]) <= right :
                q.append((nr,nc))
                visited[nr][nc] = 1
                cnt += 1
                sub_total += popular[nr][nc]
                sub_lst.append((nr,nc))

    tmp = sub_total // cnt

    if cnt > 1 :
        is_move = True
        for x,y in sub_lst :
            popular[x][y] = tmp
        # for i in range(n):
        #     print(*visited[i])
        # print(f'-----------')
        # for i in range(n):
        #     print(*popular[i])
        # print(f'-----------')


n,left,right = map(int,input().split())
popular = [list(map(int,input().split())) for _ in range(n)]


dr = [0,1,0,-1]
dc = [1,0,-1,0]
q = deque()
ans=0

while True :
    is_move = False
    visited = [[0] * n for _ in range(n)]
    for i in range(n) :
        for j in range(n) :
            sub_total = 0
            sub_lst = []
            if not visited[i][j] :
                q.append((i,j))
                visited[i][j] = 1
                sub_lst.append((i,j))
                sub_total += popular[i][j]
                bfs() # true = 움직임, false = 움직임X

    if is_move :
        ans += 1
    else :
        break

print(ans)