from collections import defaultdict, deque
from copy import deepcopy
drc = [(1,0),(-1,0),(0,1),(0,-1)]

n = int(input())
colors = [list(map(int,input().split())) for _ in range(n)]
ans = 0
# 90도 오른쪽으로 돌리기
def rotate(arr):
    tmp_n = len(arr)
    tmp = [[0]*tmp_n for _ in range(tmp_n)]

    for i in range(tmp_n):
        for j in range(tmp_n):
            tmp[j][tmp_n-1-i] = arr[i][j]

    return tmp

for _ in range(4):
    # 동일 그룹 파악
    pic_dict = defaultdict(list) # 그룹번호 : 대표번호, 갯수
    group_num = 1
    q = deque()
    visited = [[0]*n for _ in range(n)] # 그룹번호 체크
    for i in range(n):
        for j in range(n):
            if not visited[i][j] :
                q.append((i,j))
                visited[i][j] = group_num
                pic_dict[group_num] = [colors[i][j],1]

                while q:
                    r,c = q.popleft()

                    for dr,dc in drc :
                        nr = r+dr
                        nc = c+dc
                        if 0<=nr<n and 0<=nc<n and not visited[nr][nc] and colors[nr][nc] == colors[r][c]:
                            visited[nr][nc] = group_num
                            q.append((nr,nc))
                            pic_dict[group_num][1] += 1
                group_num += 1
    # print(pic_dict)
    # for z in range(n):
    #     print(*visited[z])

    # 그룹 점수 매기기
    chk = set() # 맞닿은 부분체크
    new_visited = [[0]*n for _ in range(n)]
    now_group_num = 0 # 현재 보고있는 그룹 번호

    for i in range(n):
        for j in range(n):
            if not new_visited[i][j] :
                near_group_chk = [0] * (max(pic_dict) + 1)
                new_visited[i][j] = 1
                now_group_num = visited[i][j]
                q = deque()
                q.append((i,j))

                while q :
                    r,c = q.popleft()
                    for dr,dc in drc :
                        nr = r+dr
                        nc = c+dc
                        if 0<=nr<n and 0<=nc<n and not new_visited[nr][nc]:
                            if visited[r][c] == visited[nr][nc]: # 같은 그룹이면
                                q.append((nr,nc))
                                new_visited[nr][nc] = 1
                            elif visited[r][c] != visited[nr][nc] and (r,c,nr,nc) not in chk  : #다른 그룹이고 맞닿은거 체크안했으면
                                chk.add((r,c,nr,nc))
                                chk.add((nr,nc,r,c))
                                near_group_chk[visited[nr][nc]] += 1
                # print(now_group_num,near_group_chk)
                for k in range(1,len(near_group_chk)):
                    if near_group_chk[k]:
                        ans += (pic_dict[now_group_num][1]+pic_dict[k][1])*pic_dict[now_group_num][0]*pic_dict[k][0]*near_group_chk[k]

    tmp = [[0]*n for _ in range(n)]
    #중앙가로
    mid_garo = colors[n//2][::-1]
    for i in range(n):
        tmp[i][n//2] = mid_garo[i]
    #중앙세로
    for i in range(n):
        tmp[n//2][i] = colors[i][n//2]
    cut_r = [(0,n//2),(n//2+1,n)]
    cut_c = [(0,n//2),(n//2+1,n)]
    for a,b in cut_r :
        for c,d in cut_c :
            rotated_ls = rotate([ls[c:d] for ls in colors[a:b]])
            # print(rotated_ls)
            x=y=0
            for i in range(a,b):
                for j in range(c,d):
                    tmp[i][j] = rotated_ls[x][y]
                    y += 1
                x += 1
                y=0
    colors = deepcopy(tmp)
print(ans)