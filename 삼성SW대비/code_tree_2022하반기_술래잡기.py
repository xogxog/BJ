import sys
input = sys.stdin.readline
dr = [0,0,1,-1] # 오,왼,아래,위
dc = [1,-1,0,0]
p_dr = [-1,0,1,0] # 위오아래왼
p_dc = [0,1,0,-1]
def move_doduk(sulle,police):
    tmp = [[[] for _ in range(n)] for __ in range(n)]
    # print(police)
    for i in range(n):
        for j in range(n):
            if abs(police[0]-i)+abs(police[1]-j) > 3 :
                for k in range(len(sulle[i][j])):
                    tmp[i][j].append(sulle[i][j][k])
                continue
            else:
                for k in range(len(sulle[i][j])) :
                    d = sulle[i][j][k]
                    nr = i+dr[d]
                    nc = j+dc[d]
                    if 0<=nr<n and 0<=nc<n and (nr,nc) != police :
                        tmp[nr][nc].append(d)
                    elif 0<=nr<n and 0<=nc<n and (nr,nc) == police:
                        tmp[i][j].append(d)
                    elif nr<0 or nr>=n or nc<0 or nc>=n :
                        if d == 0 :
                            if (i,j-1) != police: # 오
                                tmp[i][j-1].append(1)
                            else :
                                tmp[i][j].append(0)
                        elif d==1 :
                            if (i,j+1) != police : #왼
                                tmp[i][j + 1].append(0)
                            else :
                                tmp[i][j].append(1)
                        elif d== 2 :
                            if (i-1,j) != police :
                                tmp[i-1][j].append(3)
                            else :
                                tmp[i][j].append(2)
                        elif d==3:
                            if (i+1,j) != police :
                                tmp[i+1][j].append(2)
                            else :
                                tmp[i][j].append(3)
    return tmp
def jobgi(sulle,cnt):
    global  p_idx,ans,police
    while cnt <=k:
        # print(f'-----------------{cnt}-------------------------')
        # 도망자 움직임
        sulle = move_doduk(sulle,police)
        # print(f'도망자 움직임')
        # for z in range(n):
        #     print(*sulle[z])
        # 술래 움직임
        p_idx += 1
        if p_idx >= len(police_move):
            p_idx = 0
        police = police_move[p_idx]
        police_d = police_direc[p_idx]
        # print(f'술래 위치 및 보는 곳')
        # print(police,police_d)
        # 술래 잡기
        r, c = police
        for i in range(0,3):
            nr = r+p_dr[police_d]*i
            nc = c+p_dc[police_d]*i
            if 0<=nr<n and 0<=nc<n and not tree[nr][nc] :
                ans += cnt*len(sulle[nr][nc])
                sulle[nr][nc] = []
        # print(f'술래 잡음')
        # print(ans)
        # for z in range(n):
        #     print(*sulle[z])
        cnt += 1

n,m,h,k = map(int,input().split())
sulle = [[[] for _ in range(n)] for __ in range(n)]
tree = [[0]*n for _ in range(n)]

for _ in range(m):
    x,y,d = map(int,input().split())
    if d == 1 :
        sulle[x-1][y-1].append(0)
    else :
        sulle[x-1][y-1].append(2)
# print(f'술래')
# for z in range(n):
#     print(*sulle[z])
for _ in range(h):
    x,y = map(int,input().split())
    tree[x-1][y-1] = 1
# print('나무')
# for z in range(n):
#     print(*tree[z])
police_move = [(n // 2, n // 2)]  # 움직일 좌표
police_direc = [0]  # 경찰이 바라보는 곳
idx = 1
r, c = n // 2, n // 2

while idx < n + 1:
    for i in range(idx):  # 위
        nr = r - 1
        nc = c
        if 0 <= nr < n and 0 <= nc < n:
            police_move.append((nr, nc))
            if i + 1 == idx:
                police_direc.append(1)  # 오른쪽 봐야함
            else:
                if nr == 0 and nc == 0:
                    police_direc.append(2)
                else:
                    police_direc.append(0)
            r, c = nr, nc
    if r == 0 and c == 0:
        break
    for i in range(idx):  # 오른
        nr = r
        nc = c + 1
        police_move.append((nr, nc))
        if i + 1 == idx:
            police_direc.append(2)  # 아래
        else:
            police_direc.append(1)  # 오른
        r, c = nr, nc
    idx += 1

    for i in range(idx):  # 아래
        nr = r + 1
        nc = c
        police_move.append((nr, nc))
        if i + 1 == idx:
            police_direc.append(3)  # 왼
        else:
            police_direc.append(2)  # 아래
        r, c = nr, nc
    for i in range(idx):  # 왼
        nr = r
        nc = c - 1
        police_move.append((nr, nc))
        if i + 1 == idx:
            police_direc.append(0)  # 위
        else:
            police_direc.append(3)  # 왼
        r, c = nr, nc
    idx += 1
reverse_police_move = police_move[::-1]
police_move += reverse_police_move[1:n ** 2 - 1]
reverse_police_direc = []
# 반대방향을 딕셔너리에 묶어놓는게 좋을두루룻
for i in range(n ** 2 - 2, 0, -1):
    if police_direc[i] == 0:
        if police_direc[i] == police_direc[i - 1]:
            reverse_police_direc.append(2)
        else:
            reverse_police_direc.append(1)
    elif police_direc[i] == 3:
        if police_direc[i] == police_direc[i - 1]:
            reverse_police_direc.append(1)
        else:
            reverse_police_direc.append(0)
    if police_direc[i] == 2:
        if police_direc[i] == police_direc[i - 1]:
            reverse_police_direc.append(0)
        else:
            reverse_police_direc.append(3)
    if police_direc[i] == 1:
        if police_direc[i] == police_direc[i - 1]:
            reverse_police_direc.append(3)
        else:
            reverse_police_direc.append(2)

police_direc += reverse_police_direc
print(police_move, len(police_move))
print(police_direc, len(police_direc))
p_idx = 0
police = police_move[p_idx]
police_d = police_direc[p_idx]

ans = 0
jobgi(sulle,1)
print(ans)