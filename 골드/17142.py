# 연구소 3
# 조합 !
import sys
from collections import deque

dr = [0,0,1,-1]
dc = [1,-1,0,0]

input = sys.stdin.readline
N ,M = map(int,input().split()) # M : 놓을 수 있는 바이러스 개수

def my_bfs(q,visited) :
  global ans
  zero_cnt = 0
  
  while q :
    r,c = q.popleft()
    if visited[r][c] > ans :
      return
    else :
      for i in range(4) :
        nr = r + dr[i]
        nc = c + dc[i]
        if 0<=nr<N and 0<=nc<N and not visited[nr][nc] and lab[nr][nc] == 0 :
          visited[nr][nc] = visited[r][c] + 1
          zero_cnt += 1
          q.append((nr,nc))

  if zero_cnt == air_cnt :
    tmp_max = 0
    for z in range(N) :
      if tmp_max < max(visited[z]) :
        tmp_max = max(visited[z])
    if tmp_max < ans :
      ans = tmp_max

def my_combination(my_arr,start) :
  
  if len(my_arr) == M :
    q=deque(my_arr)
    visited = [[0]*N for _ in range(N)]
    for _j in range(M) :
      visited[my_arr[_j][0]][my_arr[_j][1]] = 1
    my_bfs(q,visited)
    return

  else :
    for _i in range(start,len(virus_loca)) :
      my_arr.append(virus_loca[_i])
      my_combination(my_arr, _i+1)
      my_arr.pop()


lab = [list(map(int,input().split())) for _ in range(N)] # 2 바이러스, 1 벽, 빈 공간
air_cnt = 0
virus_loca = [] # 바이러스 놓을 수 있는 곳
for i in range(N) :
  for j in range(N) :
    if lab[i][j] == 0 :
      air_cnt += 1
    elif lab[i][j] == 2 :
      virus_loca.append((i,j)) # 바이러스
my_arr =[] # 바이러스 놓을 곳
ans = 987654321 # 최소 이동 거리
my_combination(my_arr,0)
if ans == 987654321 :
  print(-1)
else :
  print(ans-1)