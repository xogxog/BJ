# 연구소 3
# 조합 !
# 오래걸린이유 : 비활성화된 바이러스를 뚫고 지나간다고 생각해야해서 오래걸림
# 바이러스 뚫는다면, 가장 먼 거리를 계산할때, 해당 lab이 0인지 2 인지 확인을 해야하는 점 때문에 자꾸 틀림
import sys
from collections import deque

dr = [0,0,1,-1]
dc = [1,-1,0,0]

input = sys.stdin.readline
N ,M = map(int,input().split()) # M : 놓을 수 있는 바이러스 개수

def my_bfs(q,visited) :
  global ans, last_point
  zero_cnt = 0
  
  while q :
    r,c = q.popleft()

    for i in range(4) :
      nr = r + dr[i]
      nc = c + dc[i]
      if 0<=nr<N and 0<=nc<N and not visited[nr][nc] and (lab[nr][nc] == 0 or lab[nr][nc] == 2) :
        visited[nr][nc] = visited[r][c] + 1
        q.append((nr,nc))
        if lab[nr][nc] == 0 :
          zero_cnt += 1
  # print(f'=====================')
  # for z in range(N) :
  #   print(*visited[z])

  if zero_cnt == air_cnt :
    tmp_max = 0
    for y in range(N) :
      for z in range(N) :
        if lab[y][z] == 0 and tmp_max < visited[y][z] :
          tmp_max = visited[y][z]
    if tmp_max < ans :
      ans = tmp_max
      # print(f'ans : {ans}')

def my_combination(my_arr,start) : # 바이러스 조합
  
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
if air_cnt == 0 :
  print(0)
else : 
  my_arr =[] # 바이러스 놓을 곳
  ans = 987654321 # 최소 이동 거리  
  my_combination(my_arr,0)
  if ans == 987654321 :
    print(-1)
  else :
    print(ans-1)