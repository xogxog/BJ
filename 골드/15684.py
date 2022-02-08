# 사다리 조작
def play():
    start = 0
    r,c=0,0 # r,c
    while c < N :
        while r < H :
            if c == 0 : # 가장 왼쪽 사다리인경우
                if ladder[r][c] == 1 :
                    c += 1 # 오른쪽으로 이동
                    r += 1
                else :
                    r += 1
            else :
                if ladder[r][c-1] :
                    c -= 1
                    r +=1
                elif ladder[r][c] :
                    c += 1
                    r += 1
                else :
                    r+= 1
        if start == c :
            start += 1
            c =start
            r=0
        else :
            return 0 # 출발지와 같은곳 못갔으므로
    return 1 # 모두 출발지와 같은곳에 도착한 경우

def ladder_leg(cnt) :
    global flag,ans
    if cnt >= 4 :
        ans = -1
        return
    elif flag :
        return
    for j in range(H):
        for k in range(N-1):
            if ladder[j][k] == 0 :
                if (k>=1 and (ladder[j][k-1] == 0 or ladder[j][k+1] ==0)) or (k==0 and ladder[j][k+1]==0) : # 가장 왼쪽사다리 아닌경우
                    ladder[j][k] = 1
                    check = play()
                    if check == 0 and flag == 0:
                        ladder_leg(cnt+1)
                    elif check == 1 and flag == 0 :
                        # print(check, cnt, flag)
                        flag = 1
                        ans = cnt
                        return
                    ladder[j][k] = 0

    return -1 # 모든 경우의수를 봤는데도 불가능한 경우


N,M,H = map(int,input().split()) # 세로, 가로, 세로선마다 가로선 놓을 수 있는 위치의 개수
ladder = [[0]*N for _ in range(H)]
flag = 0
cnt = 1
ans = 0
for _ in range(M):
    a,b = map(int,input().split())
    ladder[a-1][b-1] = 1 # b번과 b+1을 잇는다

tmp = play()
if tmp :
    print(0)
else :
    ladder_leg(cnt)
    print(ans)


