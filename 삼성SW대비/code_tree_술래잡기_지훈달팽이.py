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
        # 도망자 움직임
        sulle = move_doduk(sulle,police)
        # 술래 움직임
        p_idx += 1
        if p_idx >= len(police_move):
            p_idx = 0
        police = police_move[p_idx]
        police_d = police_direc[p_idx]
        # 술래 잡기
        r, c = police
        for i in range(0,3):
            nr = r+p_dr[police_d]*i
            nc = c+p_dc[police_d]*i
            if 0<=nr<n and 0<=nc<n and not tree[nr][nc] :
                ans += cnt*len(sulle[nr][nc])
                sulle[nr][nc] = []
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

for _ in range(h):
    x,y = map(int,input().split())
    tree[x-1][y-1] = 1

police_move = []  # 움직일 좌표
police_direc = []  # 경찰이 바라보는 곳
r = c = n // 2
d = 0
for i in range(2,2*n+1):
    for j in range(i//2):
        police_move.append((r,c))
        police_direc.append(d)
        r += p_dr[d]
        c += p_dc[d]
    d = (d+1)%4
# police_move = police_move[:n**2-1]
police_direc = police_direc[:n**2-1]
r = c = 0
d = 2
rev_p_move = []
rev_p_direc = []
for i in range(2*n,1,-1):
    for j in range(i//2):
        if j == n-1 :
            continue
        rev_p_move.append((r,c))
        rev_p_direc.append(d)
        r += p_dr[d]
        c += p_dc[d]
    d -= 1
    if d < 0 :
        d = 3
print(rev_p_direc)
police_move += rev_p_move[1:n**2-1]
police_direc += rev_p_direc[:n**2-1]

print(police_move,len(police_move))
print(police_direc,len(police_direc))

p_idx = 0
police = police_move[p_idx]
police_d = police_direc[p_idx]

ans = 0
jobgi(sulle,1)
print(ans)