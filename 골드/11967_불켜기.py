import sys
from collections import defaultdict, deque
input = sys.stdin.readline

drc = [(0,1),(0,-1),(1,0),(-1,0)]

N,M = map(int,input().split())
_dic = defaultdict(list)

light = [[0]*N for _ in range(N)]
move = [[0]*N for _ in range(N)]
visited = [[0] * N for _ in range(N)]

for _ in range(M):
    x,y,a,b = map(int,input().split())
    _dic[(x-1,y-1)].append((a-1,b-1))

light[0][0] = 1
visited[0][0] = 1
move[0][0] = 1

q = deque()
q.append((0,0))
ans = 1
while q :
    r,c = q.popleft()

    move[r][c] = 1

    for rr,cc in _dic[(r,c)]: # 방문한 방에서 불 다 켜기
        if light[rr][cc] == 0 :
            ans += 1
            light[rr][cc] = 1

    for i in range(4): # 현재 위치에서 돌아다닐 수 있는 위치 체크
        nr = r+drc[i][0]
        nc = c+drc[i][1]
        if 0<=nr<N and 0<=nc<N :
            move[nr][nc] = 1

    # 전체 돌면서 방문 가능한 곳(불 켤 수 있는 곳) 체크해서 q에 넣어주기
    for j in range(N):
        for k in range(N):
            if light[j][k] and move[j][k] and not visited[j][k]: # 방 불 켜져있고, 움직일 수 있고, 아직 vistied 하지 않았으면
                visited[j][k] = 1 # 방문처리하고
                q.append((j,k))

print(ans)