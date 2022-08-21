import sys
from itertools import permutations
input = sys.stdin.readline

# 우 하 좌 상
dr = [0,1,0,-1]
dc = [1,0,-1,0]

def rot_2(arr,s) :
    tmp = [[0]*(s*2+1) for _ in range(s*2+1)]
    visited = [[0] * (s * 2 + 1) for _ in range(s * 2 + 1)]
    tmp[s][s] = arr[s][s]
    visited[s][s] = 1
    r,c = 0,0
    sr,sc = r,c
    idx = 0
    while 1 :
        nr = r+dr[idx]
        nc = c+dc[idx]
        # print(nr,nc)
        if 0<=nr<(s*2+1) and 0<=nc<(s*2+1) and not visited[nr][nc] :
            if idx == 0 : # 우방향인 경우 왼쪽꺼
                tmp[nr][nc] = arr[nr][nc-1]
            elif idx == 1 : # 하방향인 경우 위에 값
                tmp[nr][nc] = arr[nr-1][nc]
            elif idx == 2 : # 좌 / 우
                tmp[nr][nc] = arr[nr][nc+1]
            elif idx == 3 : # 상 / 하
                tmp[nr][nc] = arr[nr+1][nc]
            visited[nr][nc] = 1
            r = nr
            c = nc
        else :
            idx = (idx+1) % 4

        if sr == r and sc == c :
            r += 1
            c += 1
            sr,sc = r,c
            idx = 0
            if r == s and c == s :
                break

    return tmp





def rot(arr): # ([3, 4, 2], [4, 2, 1])
    global ls
    tmp_ls = [l[:] for l in ls] # deepcopy
    for i in range(len(arr)) :
        r,c,s = arr[i]
        r -= 1
        c -= 1
        tmp_2 = [t[c-s:c+s+1]for t in tmp_ls[r-s:r+s+1]]
        tmp_3 = rot_2(tmp_2,s)
        x,y = 0,0
        for j in range(r-s,r+s+1):
            for k in range(c-s,c+s+1):
                tmp_ls[j][k] = tmp_3[x][y]
                y += 1
            x += 1
            y = 0

    return tmp_ls



N,M,K = map(int,input().split())
ls = [list(map(int,input().split())) for _ in range(N)]
rotation = []

for _ in range(K):
    rotation.append(list(map(int,input().split())))
rot_per = list(permutations(rotation,len(rotation)))
# print(rot_per)
ans = 987654321
for i in range(len(rot_per)):
    arr = rot(rot_per[i])
    for z in range(len(arr)) :
        if ans > sum(arr[z]):
            ans = sum(arr[z])

print(ans)