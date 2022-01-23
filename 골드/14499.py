from collections import deque

def copy_dice_or_map(d) :
    if d == 'west' or d =='east':
        if my_map[nr][nc] == 0:  # 맵에 쓰여진게 0이면
            my_map[nr][nc] = dice_r[3]
        elif my_map[nr][nc] != 0:
            dice_r[3] = my_map[nr][nc]
            my_map[nr][nc] = 0
        dice_c[3] = dice_r[3]
        dice_c[1] = dice_r[1]
        print(dice_r[1])
    else :
        if my_map[nr][nc] == 0 :
            my_map[nr][nc] = dice_c[3]
        elif my_map[nr][nc] != 0:
            dice_c[3] = my_map[nr][nc]
            my_map[nr][nc] = 0
        dice_r[3] = dice_c[3]
        dice_r[1] = dice_c[1]
        print(dice_c[1])

n,m,x,y,k = map(int,input().split()) # 세로, 가로, 주사위좌표, 명령 개수
my_map = [list(map(int,input().split())) for _ in range(n) ]
# 동 서 북 남
dr = [0,0,0,-1,1]
dc = [0,1,-1,0,0]
direction = list(map(int,input().split())) # 방향
dice_r = deque([0,0,0,0])
dice_c = deque([0,0,0,0])

for direc in direction :
    nr = x + dr[direc]
    nc = y + dc[direc]

    if 0<= nr <n and 0<=nc<m :

        if direc == 1 : # 동
            dice_r.rotate(1) # 주사위 돌리기
            copy_dice_or_map('east')

        elif direc == 2 : # 서
            dice_r.rotate(-1)
            copy_dice_or_map('west')

        elif direc == 3 : # 북
            dice_c.rotate(-1)
            copy_dice_or_map('north')
        else : # 남
            dice_c.rotate(1)
            copy_dice_or_map('south')

        x,y = nr,nc