import sys
input = sys.stdin.readline

def attack(archers, castle) :
    global ans
    tmp_castle = [c[:] for c in castle]

    tmp_cnt = 0
    flag = 1

    while flag :
        tmp_sum = 0
        ls = [[0, M - 1], [0, M - 1], [0, M - 1]]  # 궁수별 공격할 적 위치 - 가장 먼 위치로 초기화
        for i in range(N):
            for j in range(M):
                if tmp_castle[i][j] == 1 :
                    tmp_sum += 1
                    for k in range(len(archers)) :
                        _origin = abs(ls[k][0]-archers[k][0])+abs(ls[k][1]-archers[k][1])
                        _now = abs(i-archers[k][0])+abs(j-archers[k][1])
                        if _now <=D : # 궁수 공격 거리 안
                            if _now == _origin and j<ls[k][1] : # 공격 거리 같으면 왼쪽 적 공격
                                ls[k] = [i,j]
                            elif _now < _origin :
                                ls[k] = [i,j]

        if tmp_sum == 0 : # 공격할 적이 없다면 끝
            flag = 0
            break
        # 공격한 적 없애고 적 카운트
        for l in range(len(ls)) :
            if tmp_castle[ls[l][0]][ls[l][1]] and abs(ls[l][0]-archers[l][0])+abs(ls[l][1]-archers[l][1])<=D :
                tmp_cnt += 1
                tmp_castle[ls[l][0]][ls[l][1]] = 0

        # 적 이동
        move = []
        for m in range(N) :
            for n in range(M) :
                if tmp_castle[m][n] :
                    if m+1 >= N : # 성 있는 칸으로 이동시 게임에서 제외
                        tmp_castle[m][n] = 0
                    else :
                        move.append((m,n))

        for o in range(len(move)) :

            tmp_castle[move[o][0]][move[o][1]] -= 1
            tmp_castle[move[o][0]+1][move[o][1]] += 1

    if ans < tmp_cnt :
        ans = tmp_cnt

def archer(ls, idx,cnt) :
    global castle
    if cnt == 3 :
        attack(ls, castle)
        return

    for i in range(idx, M) :
        ls[cnt] = [N,i] # 궁수 위치
        # print(ls)
        archer(ls,i+1,cnt+1)




N,M,D = map(int,input().split()) # 행, 열, 거리 제한
castle = [list(map(int,input().split())) for _ in range(N)]
ans = 0

archers = [[],[],[]]
archer(archers,0,0)
print(ans)