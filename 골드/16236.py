from collections import deque

def eat_fish() :
    global baby_shark, cnt_eat_fish, shark_size, time
    visited = [[0] * N for _ in range(N)]
    q=deque()
    q.append(baby_shark)

    can_eat_fish=[] # 가장 가까운 거리에 있는 물고기 위치
    flag = 0
    # 가장 가까운 물고기 탐색
    while q :

        r,c,cnt = q.popleft()
        visited[r][c] = 1

        if len(can_eat_fish) and can_eat_fish[-1][2] < cnt+1 : # 마지막으로 들어간 거리가 지금 갈곳의 거리보다 크다면 반복문 종료
            break
        for k in range(4) :
            nr = r+dr[k]
            nc = c+dc[k]
            # 상어 지나감
            if 0<=nr<N and 0<=nc<N and not visited[nr][nc] and ocean[nr][nc] <= shark_size :
                visited[nr][nc] = 1
                q.append([nr,nc,cnt+1])
                if ocean[nr][nc] !=0 and ocean[nr][nc] < shark_size :
                    can_eat_fish.append([nr,nc,cnt+1])

    if len(can_eat_fish) == 0 : # 먹을 물고기 없으면 함수 종료
        return [987654321]
    else :
        if len(can_eat_fish) > 1 :
            # 가장 윗쪽 -> 여러마리라면 가장 왼쪽 것을 먹음
            can_eat_fish.sort(key=lambda x : x[1])
            can_eat_fish.sort(key=lambda x: x[0])
        tmp_baby_shark = [can_eat_fish[0][0],can_eat_fish[0][1],0] # 아기상어 위치 바꿔줌
        ocean[can_eat_fish[0][0]][can_eat_fish[0][1]] = 0 #먹은 물고기 없애기
        cnt_eat_fish += 1 # 먹은 물고기 갯수
        time += can_eat_fish[0][2] # 이동한 만큼 시간 올리기
        if cnt_eat_fish == shark_size : # 아기상어 사이즈 올리기
            shark_size += 1
            cnt_eat_fish = 0
        return tmp_baby_shark

N = int(input())
ocean = list(list(map(int,input().split())) for _ in range(N))

time = 0
shark_size = 2
cnt_eat_fish = 0
tmp_baby_shark = []
dr = [1,-1,0,0]
dc = [0,0,1,-1]

# 아기 상어 위치
for i in range(N):
    for j in range(N):
        if ocean[i][j] == 9 :
            baby_shark=[i,j,0] # 상어 좌표, 상어와 떨어진 거리
            ocean[i][j] = 0 # 상어 없애기

while tmp_baby_shark != [987654321]:
    tmp_baby_shark = eat_fish()
    baby_shark = tmp_baby_shark

print(time)