# 색종이 붙이기
import sys
input = sys.stdin.readline

# 제일 큰 색종이 부터 붙이는 방법 -> 실패

# def check(idx):
#     for i in range(10-idx+1):
#         for j in range(10-idx+1):
#             if ls[i][j] == 1 :
#                 tmp = [row[j:j+idx] for row in ls[i:i+idx]]
#                 # print(f'i:{i}, j:{j}, tmp:{tmp}')
#                 # 색종이 놓을 수 있는지 check
#                 flag = 0
#                 for k in range(idx):
#                     for l in range(idx):
#                         if tmp[k][l] == 0 :
#                             flag = 1
#                             break
#                     if flag :
#                         break
#                 # 색종이 못 놓음
#                 if flag :
#                     continue
#                 # 색종이 놓을 수 있음
#                 else:
#                     if color_paper[idx]: # 색종이 남은 경우
#                         color_paper[idx] -= 1
#                         for m in range(i,i+idx):
#                             for n in range(j,j+idx):
#                                 ls[m][n] = 0


def StickTorF(r,c,i):
    for j in range(r, r + i):
        for k in range(c, c + i):
            if ls[j][k] == 0 :
                return False
    return True

def tracking(r,c,used): # 행,열
    global tmp_ans
    if r >= 10 :
        tmp_ans = min(tmp_ans,used)
        return
    if c >= 10 :
        tracking(r+1,0,used)
        return
    if ls[r][c] :
        for i in range(5,0,-1):
            # 색종이 여분
            if color_paper[i] == 0:
                continue
            # 범위 체크
            if r+i-1>=10 or c+i-1>=10 :
                continue
            if StickTorF(r,c,i) : # 색종이 붙일 수 있으면
                for j in range(r, r + i):
                    for k in range(c, c + i):
                        ls[j][k]=0
                color_paper[i] -= 1
                # print(f'==============')
                # for z in range(10):
                #     print(*ls[z])
                tracking(r,c+i,used+1)
                color_paper[i] += 1
                for j in range(r, r + i):
                    for k in range(c, c + i):
                        ls[j][k]=1
    else :
        tracking(r,c+1,used)





color_paper = [0,5,5,5,5,5] # 색종이 크기별 갯수
tmp_ans = 25
ls = [list(map(int,input().split())) for _ in range(10)]

# for i in range(5,0,-1):
#     check(i)

tracking(0,0,0)

if tmp_ans == 25:
    print(-1)
else:
    print(tmp_ans)
