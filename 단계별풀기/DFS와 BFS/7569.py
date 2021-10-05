# 7569. 토마토
from collections import deque
dx = [0,0,-1,1,0,0]
dy = [1,-1,0,0,0,0]
dz = [0,0,0,0,1,-1]



def tomato():


    while q :
        x,y,z = q.popleft()

        for m in range(6) :
            mx = x + dx[m]
            my = y + dy[m]
            mz = z + dz[m]
            if ls[mx][my][mz] == -1 :
                continue
            elif 0<=mx<M and 0<=my<N and 0<=mz<H and ls[mx][my][mz] :





M,N,H = map(int,input().split()) # 가로, 세로 , 높이

ls = [[list(map(int,input().split())) for _ in range(N)] for _ in range(H)]

q = deque()

for i in range(len(ls)) :
    for j in range(len(ls[i])):
        for k in range(len(ls[i][j])) :
          if[i][j][k] == 1 :
            q.append((i,j,k))

tomato()