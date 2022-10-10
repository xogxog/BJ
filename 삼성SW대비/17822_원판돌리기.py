import sys
from collections import deque
input = sys.stdin.readline

drc = [(0,1),(0,-1),(1,0),(-1,0)]
def turn_grid(ls,d,k):
    if d == 0 : # 시계방향
        tmp_1 = ls[m-k:]
        tmp_2 = ls[:m-k]
        return tmp_1+tmp_2
    else : # 반시계방향
        tmp_1 = ls[0:k]
        tmp_2 = ls[k:]
        return tmp_2+tmp_1

n, m, t = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
clean_grid = 0
for _ in range(t):
    x, d, k = map(int, input().split())  # 배수, 방향, k칸

    idx = 1
    # 돌리기
    while 1 :
        if (x*idx)-1 < n :
            grid[(x*idx)-1] = turn_grid(grid[(x*idx)-1],d,k)
        else :
            break
        idx += 1
    # 인접한 수 찾아서 없애기
    flag = 0 # 인접한 수 있는지 체크
    for i in range(n):
        for j in range(m):
            if not grid[i][j] :
                continue
            r,c = i,j
            curr_num = grid[r][c]
            q = deque([(r,c)])
            d_set = set()
            while q:
                rr,cc = q.popleft()
                for dr,dc in drc :
                    nr = rr+dr
                    nc = cc+dc
                    if nc<0 :
                        nc = m-1 # 마지막
                    elif nc>=m :
                        nc = 0   # 첫번째
                    if 0<=nr<n :
                        if curr_num == grid[nr][nc] and (nr,nc) not in d_set :
                            d_set.add((nr,nc))
                            q.append((nr,nc))
            if d_set :
                flag = 1
                grid[r][c] = 0
                for nr,nc in d_set:
                    grid[nr][nc] = 0

    if not flag : # 인접한 수 없음
        cnt_num = 0
        tmp_sum = 0
        for i in range(n):
            cnt_num += m-(grid[i].count(0))
            tmp_sum += sum(grid[i])
        if cnt_num != 0 :
            tmp_avg = tmp_sum/cnt_num

            for i in range(n):
                for j in range(m):
                    if grid[i][j]:
                        if grid[i][j] > tmp_avg:
                            grid[i][j] -= 1
                        elif grid[i][j] < tmp_avg :
                            grid[i][j] += 1
        else :
            clean_grid = 1
            break
if clean_grid :
    print(0)
else :
    ans = 0
    for i in range(n):
        ans += sum(grid[i])
    print(ans)
    # print(sum(map(sum, grid)))