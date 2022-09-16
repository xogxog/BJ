import sys
from collections import defaultdict, deque
input = sys.stdin.readline

drc = [(0,1),(0,-1),(1,0),(-1,0)]

def light(x,y):

    q = deque()
    q.append((x,y))

    while q :
        r,c = q.popleft()

        for i in range(4):
            nr = r+drc[i][0]
            nc = c+drc[i][1]

            if (nr == 0 and nc == 0) or (nr,nc) in light_on : # 출발 지점에서 이어진 곳이라면
                light_on.add((x, y))
                visited[x][y] = 1
                return True

            if 0<=nr<N and 0<=nc<N and visited[nr][nc] and room[nr][nc] :
                # visited[nr][nc] = 1
                q.append((nr,nc))

    return False

N,M = map(int,input().split())
_dic = defaultdict(list)
room = [[0]*N for _ in range(N)]
visited = [[0] * N for _ in range(N)]
light_on = set()
light_on.add((0,0))

for _ in range(M):
    x,y,a,b = map(int,input().split())
    _dic[(x-1,y-1)].append((a-1,b-1))

room[0][0] = 1
q = deque()
q.append((0,0))
visited[0][0] = 1
while q :
    r,c = q.popleft()

    for rr,cc in _dic[(r,c)]: # 방문한 방에서 불 다 켜기
        room[rr][cc] = 1

    for rrr,ccc in _dic[(r,c)] :
        TorF = light(rrr,ccc)
        if TorF :
            q.append((rrr,ccc)) # 옮겨 다닐 수 있는 위치

print(len(light_on))
