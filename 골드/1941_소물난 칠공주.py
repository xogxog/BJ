import sys
input = sys.stdin.readline

dr = [0,0,1,-1]
dc = [1,-1,0,0]
# 이다솜파 4명 이상 -> 'S'

def dfs(r,c,s,y,cnt) :
    global ans

    if y>3 :
        return

    if s+y == 7 :
        if s >= 4 :
            ans += 1
        return

    for i in range(4) :
        nr = r + dr[i]
        nc = c + nr[i]
        if 0<=nr<5 and 0<=nc<5 and not visited[nr][nc] :
            visited[nr][nc]=1
            if princess[nr][nc] =="Y" :
                dfs(nr,nc,s,y+1,cnt +1)
            else :
                dfs(nr, nc, s+1, y, cnt + 1)
            visited[nr][nc] = 0

princess = [input().rstrip() for _ in range(5)]
ans = 0

visited = [[0]*5 for i in range(5)]
visited[0][0] = 1
if princess[0][0] == 'Y' :
    dfs(0,0,0,1,1)
else :
    dfs(0, 0, 1, 0, 1)
