from collections import deque
import os
tmp_drc = [(1,0),(0,1),(-1,0),(0,-1)] #아래 오른 위 왼
gong_drc = [(0,1),(-1,0),(0,-1),(1,0)] #오른 위 왼 아래

n,m,k = map(int,input().split())
ggori = [list(map(int,input().split())) for _ in range(n)]
gong = [(0),(0,0,0)] # 라운드 별 공던지기 r,c,d

round_idx = 1
ans = 0

q = deque()
q.append((0,0))
d = 0
for _ in range(n*4-1):
    r,c = q.popleft()
    nr = r+tmp_drc[d][0]
    nc = c+tmp_drc[d][1]
    if 0<=nr<n and 0<=nc<n :
        q.append((nr,nc))
        gong.append((nr,nc,d))
    else :
        q.append((r,c))
        d += 1
        gong.append((r,c,d))

for round in range(1,k+1):

    # 머리따라서 한칸씩 이동
    visited = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if ggori[i][j] == 1 and not visited[i][j]:
                q = deque()
                visited[i][j] = 1
                q.append((i,j,ggori[i][j]))
                while q :
                    r,c,curr = q.popleft()
                    # print(r,c,curr)
                    if curr == 1:
                        for dr,dc in tmp_drc:
                            nr = r+dr
                            nc = c+dc
                            if 0<=nr<n and 0<=nc<n and ggori[r][c]+1 < ggori[nr][nc] :
                               q.append((nr,nc,ggori[nr][nc]))
                               visited[nr][nc] = 1
                               ggori[r][c] = 2
                               ggori[nr][nc] = curr
                    else :
                        for dr,dc in tmp_drc:
                            nr = r+dr
                            nc = c+dc
                            if 0<=nr<n and 0<=nc<n and not visited[nr][nc] and ggori[nr][nc] :
                               q.append((nr,nc,ggori[nr][nc]))
                               visited[nr][nc] = 1
                               ggori[nr][nc] = curr
    # print(f'이동후')
    # for z in range(n):
    #     print(*ggori[z])

    # 공 맞추기
    r,c,d = gong[round_idx]

    for i in range(n):
        nr = r+gong_drc[d][0]*i
        nc = c+gong_drc[d][1]*i
        # print(nr,nc,ggori[nr][nc])
        if 0<ggori[nr][nc] <4 : #사람이 맞은 경우

            visited_2 = [[0]*n for _ in range(n)]
            q_2 = deque()
            q_2.append((nr,nc,1))
            visited_2[nr][nc] = 1
            ppl_ls = [] # 줄 서있는 좌표
            ppl_num = [] # 줄 서있는 넘버
            while q_2 :
                rr,cc,distance = q_2.popleft()

                if ggori[rr][cc] == 1 :
                    ans += distance**2
                    ppl_ls.append((rr,cc))
                    ppl_num.append(1)
                    break
                for ddr,ddc in tmp_drc :
                    nnr = rr+ ddr
                    nnc = cc+ ddc
                    if 0<=nnr<n and 0<=nnc<n and not visited_2[nnr][nnc] and (ggori[rr][cc]==ggori[nnr][nnc] or ggori[rr][cc] == ggori[nnr][nnc]+1) and ggori[nnr][nnc] != 0:
                        visited_2[nnr][nnc] = 1
                        q_2.append((nnr,nnc,distance+1))
            # 방향 바꿔주기
            q_3 = deque()
            q_3.append(ppl_ls[0])
            visited_set = set()
            visited_set.add(ppl_ls[0])

            while q_3 :
                rrr,ccc = q_3.popleft()

                for dr,dc in tmp_drc :
                    nnnr = rrr+dr
                    nnnc = ccc+dc
                    if 0<=nnnr<n and 0<=nnnc<n and (nnnr,nnnc) not in visited_set and ggori[nnnr][nnnc] != 4 and (ggori[rrr][ccc] == ggori[nnnr][nnnc] or ggori[rrr][ccc]+1 == ggori[nnnr][nnnc]) :
                        visited_set.add((nnnr,nnnc))
                        q_3.append((nnnr,nnnc))
                        ppl_ls.append((nnnr,nnnc))
                        ppl_num.append(ggori[nnnr][nnnc])

            rev_ppl_num = list(reversed(ppl_num))
            for i in range(len(ppl_ls)):
                ggori[ppl_ls[i][0]][ppl_ls[i][1]] = rev_ppl_num[i]


            break
    round_idx += 1
    if round_idx > n*4 :
        round_idx = 1

print(ans)