# 낚시왕
# 좌표마다 넣고 빼고 하지말고 좌표 계산한 후에 넣어주는 방식 !
import sys
input = sys.stdin.readline

# 위 , 아래, 오, 왼
dr = [-1,1,0,0]
dc = [0,0,1,-1]

def moving(person_loca) :
    global ans
    tmp_ocean = [[0]*C for _ in range(R)]
    # 사람이 상어잡기
    for _i in range(R) :
        if ocean[_i][person_loca] != 0 :
            ans += ocean[_i][person_loca][2]
            ocean[_i][person_loca] = 0
            break

    # 상어 이동
    for _j in range(R) :
        for _k in range(C) :
            if ocean[_j][_k] != 0 : # 해당 칸에 상어가 있다면
                origin_s = ocean[_j][_k][0]
                r,c,s,d,z = _j,_k,ocean[_j][_k][0],ocean[_j][_k][1],ocean[_j][_k][2]
                while s>0 :
                    # 정방향으로 이동
                    r += dr[d]
                    c += dc[d]
                    if 0<=r<R and 0<=c<C :
                        s -= 1
                    else :
                        # 정방향으로 이동했으니까 다시 백한 후, 방향 전환만
                        r -= dr[d]
                        c -= dc[d]
                        if d==0 : d = 1
                        elif d==1 : d = 0
                        elif d==2 : d = 3
                        elif d==3 : d = 2
                if tmp_ocean[r][c] == 0 :
                    tmp_ocean[r][c] = [origin_s,d,z]
                else :
                    if tmp_ocean[r][c][2] < z :
                        tmp_ocean[r][c] = [origin_s,d,z]
    return tmp_ocean


R,C,M = map(int,input().split())
ocean = [[0]*C for _ in range(R)]

ans = 0
for _ in range(M) :
    r,c,s,d,z = map(int,input().split())
    ocean[r-1][c-1]=[s,d-1,z] # 속력, 이동 방향, 크기

for i in range(C) :
    ocean = moving(i)
print(ans)