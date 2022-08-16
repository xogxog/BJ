import sys
input = sys.stdin.readline

dr = [0,0,1,-1]
dc = [1,-1,0,0]
# 이다솜파 4명 이상 -> 'S'

def dfs(s,y,ls) :
    global ans

    if y>3 :
        return

    if s+y == 7 :
        ls.sort()
        ans.add(tuple(ls))
        return

    for r,c in ls :
        for i in range(4) :
            nr = r + dr[i]
            nc = c + dc[i]
            if 0<=nr<5 and 0<=nc<5 and not visited[nr][nc] :
                visited[nr][nc]=1
                if princess[nr][nc] =="Y" :
                    dfs(s,y+1,ls+[(nr,nc)])
                else :
                    dfs(s+1,y,ls+[(nr,nc)])
                visited[nr][nc] = 0

princess = [input().rstrip() for _ in range(5)]
ans = set()
visited = [[0]*5 for _ in range(5)]

for i in range(5) :
    for j in range(5):
        if not visited[i][j] :
            visited[i][j] = 1
            if princess[i][j] == 'Y' :
                dfs(0,1,[(i,j)])
            else :
                dfs(1, 0,[(i,j)])
            visited[i][j] = 0

print(len(ans))