def dfs(d):
    global cnt, flag
    if flag:
        return
    curr_r, curr_c = stack.pop()
    for _ in range(4):
        nd =(d+1)%4
        nr = curr_r+dr[nd]
        nc = curr_c+dc[nd]

        if 0<=nr<n and 0<=nc<m and not visited[nr][nc] and room[nr][nc] == 0 : # 범위안에 있고, 방문하지 않았고, 벽이 아니라면
            stack.append([nr,nc])
            visited[nr][nc] = 1
            cnt += 1
            dfs(nd)
            return # 다시 돌아나올 일 없으므로 return
        d = nd # 방향 전환
    # 네 방향다 돌고 나왔을 때 다 청소 했다면
    # 후진
    nd = (d+2) % 4
    nr = curr_r + dr[nd]
    nc = curr_c + dc[nd]
    if room[nr][nc] == 1 : # 벽이면
        flag = 1
        return
    # elif 0<=nr<n and 0<=nc<m and room[nr][nc] == 0 : # 벽이아니면 후진
    stack.append([nr,nc])
    dfs(d) # 방향 유지한 채로 후진


n,m = map(int,input().split()) # 세로 / 가로
r,c,d = map(int,input().split()) # r : 행 / c : 열
if d == 1 :
    d = 3
elif d == 3 :
    d = 1
room = list(list(map(int,input().split())) for _ in range(n))
visited = [[0]*m for _ in range(n)]
flag = 0
# 북 서 남 동 순서
dr = [-1,0,1,0]
dc = [0,-1,0,1,0]

# 처음 시작하는 곳 방문 처리
visited[r][c] = 1
cnt = 1
stack =[[r,c]] # 스택에 넣어주기
dfs(d)
print(cnt)

