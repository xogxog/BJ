from copy import deepcopy
dr = [-1,-1,0,1,1,1,0,-1]
dc = [0,-1,-1,-1,0,1,1,1]

def eat_fish(grid, tmp_ans,shark):
    global ans
    # 물고기 이동
    idx = 1
    while idx <= 16 :
        f_flag = 0
        for i in range(4):
            for j in range(4):
                if len(grid[i][j]) and grid[i][j][0] == idx : # 해당 번호의 물고기를 찾으면
                    r,c = i,j
                    direct =grid[i][j][1]
                    for _ in range(8):
                        nr = r + dr[direct]
                        nc = c + dc[direct]
                        # 다른 물고기 있거나, 빈칸인 경우
                        if 0<=nr<4 and 0<=nc<4 and (len(grid[nr][nc])==0 or grid[nr][nc][0] < 17) :
                            grid[r][c], grid[nr][nc] = grid[nr][nc], [grid[r][c][0],direct] # 자리 스위치
                            f_flag = 1
                            break
                        # 공간을 넘거나, 상어가 있는 경우
                        else :
                            direct = (direct+1) % 8
                if f_flag :
                    break
            if f_flag :
                break
        idx += 1

    # 상어이동
    s_r,s_c,s_d = shark
    ate_fish = []
    flag = 0
    for i in range(1,4): # 상어가 최대 3칸 움직일 수 있으므로
        s_nr = s_r + (i*dr[s_d])
        s_nc = s_c + (i*dc[s_d])
        # 범위 안이고 물고기가 있다면
        if 0<=s_nr<4 and 0<=s_nc<4 and len(grid[s_nr][s_nc]) :
            # 여기서 tmp_grid = deepcopy(grid)를하면 44,45,49,50번째 줄은 필요가 없다.
            flag = 1
            ate_fish = grid[s_nr][s_nc]
            new_direct = grid[s_nr][s_nc][1]
            grid[s_nr][s_nc] = [17,new_direct] # 상어 이동한 곳으로 집어 넣기
            grid[s_r][s_c] = [] # 상어 있던곳 비우기
            eat_fish(deepcopy(grid),tmp_ans+ate_fish[0],[s_nr,s_nc,ate_fish[1]])
            grid[s_r][s_c] = [17,s_d]
            grid[s_nr][s_nc] = ate_fish

    if not flag : # 갈곳이 없음
        ans = max(tmp_ans,ans)
        return

grid = [[[] for _ in range(4)] for __ in range(4)]
for _ in range(4):
    tmp = list(map(int,input().split()))
    for i in range(4):
        grid[_][i] = [tmp[i*2]]+[tmp[i*2+1]-1]
ans = 0
direc = grid[0][0][1]
tmp_ate_fish = grid[0][0][0]
grid[0][0] = [17,direc]
eat_fish(grid,tmp_ate_fish,[0,0,direc])
print(ans)