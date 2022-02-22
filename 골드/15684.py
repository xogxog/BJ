import sys
# 사다리 조작
def play():

    for i in range(N) :
        now = i

        for j in range(H):
            if ladder[j][now] == 1:
                now += 1
            elif now > 0 and ladder[j][now-1] :
                now -= 1

        if now != i :
            return False
    return True

def ladder_leg(cnt,start) :
    global flag,ans
    if cnt >= 4 :
        ans = -1
        return

    # 사다리 가로로 다리 놓음
    for j in range(start,H):
        for k in range(N-1):
            if ladder[j][k] == 0 :
                if (k>=1 and (ladder[j][k-1] == 0 or ladder[j][k+1] ==0)) or (k==0 and ladder[j][k+1]==0) :
                    ladder[j][k] = 1
                    check = play()
                    if not check and flag == 0:
                        ladder_leg(cnt+1, start+1)
                    elif check and flag == 0 :
                        # print(check, cnt, flag)
                        flag = 1
                        ans = cnt
                        return
                    ladder[j][k] = 0
                    if flag :
                        print(ans)
                        exit(0)
                        return

    return -1 # 모든 경우의수를 봤는데도 불가능한 경우


N,M,H = map(int,input().split()) # 세로, 가로, 세로선마다 가로선 놓을 수 있는 위치의 개수
ladder = [[0]*N for _ in range(H)]
flag = 0
cnt = 1
ans = 0
for _ in range(M):
    a,b = map(int,sys.stdin.readline().split())
    ladder[a-1][b-1] = 1 # b번과 b+1을 잇는다

tmp = play()
if tmp :
    print(0)
else :
    ladder_leg(cnt,0)
    print(ans)


