# 낮출 수 있는 차원은 낮출 수 있으면 낮추자! 차원을 낮춰...........제발...........................
import sys
input = sys.stdin.readline
# 위, 아래, 앞, 뒤, 왼, 오
dice = [[['']*3 for _i in range(3)] for _ in range(6)]


def set_dice():
    dice = [
        [['w']*3 for _i in range(3)],
        [['y']*3 for _i in range(3)],
        [['r']*3 for _i in range(3)],
        [['o']*3 for _i in range(3)],
        [['g']*3 for _i in range(3)],
        [['b']*3 for _i in range(3)],
    ]


def roll_circle(side, direc):

    tmp = [['']*3 for _i in range(3)]
    ls = []

    if direc == '+':  # 시계방향
        for i in range(3):
            ls = dice[side][:]
            for j in range(3):
                for k in range(3):
                    tmp[k][2-j] = ls[j][k]
    else:  # 반시계방향
        for i in range(3):
            ls = dice[side][:]
            for j in range(3):
                for k in range(3):
                    tmp[2-k][j] = ls[j][k]

    dice[side] = [t[:] for t in tmp]  # 돌린거 저장!


def roll_d(side, s1, s2, s3, s4, direc):

    tmp = [0, 0, 0]
    if side == 0:  # 위 앞,왼,뒤,오
        # 시계방향
        if direc == '+':
            tmp = dice[s1][0][:]
            dice[s1][0] = dice[s4][0][:]
            dice[s4][0] = dice[s3][0][:]
            dice[s3][0] = dice[s2][0][:]
            dice[s2][0] = tmp[:]
        # 반시계방향
        else:
            tmp = dice[s1][0][:]
            dice[s1][0] = dice[s2][0][:]
            dice[s2][0] = dice[s3][0][:]
            dice[s3][0] = dice[s4][0][:]
            dice[s4][0] = tmp[:]

    elif side == 1:  # 아래 (앞,오,뒤,왼)
        # 시계방향
        if direc == '+':
            tmp = dice[s1][2][:]
            dice[s1][2] = dice[s4][2][:]
            dice[s4][2] = dice[s3][2][:]
            dice[s3][2] = dice[s2][2][:]
            dice[s2][2] = tmp[:]
        # 반시계방향
        else:
            tmp = dice[s1][2][:]
            dice[s1][2] = dice[s2][2][:]
            dice[s2][2] = dice[s3][2][:]
            dice[s3][2] = dice[s4][2][:]
            dice[s4][2] = tmp[:]
    elif side == 2:  # 앞 (위,오,아래,왼)
        # 시계방향
        if direc == '+':
            tmp = dice[s1][2][:]
            for i in range(3):
                dice[s1][2][i] = dice[s4][2-i][2]
            for i in range(3):
                dice[s4][i][2] = dice[s3][0][i]
            for i in range(3):
                dice[s3][0][i] = dice[s2][2-i][0]
            for i in range(3):
                dice[s2][i][0] = tmp[i]
        # 반시계방향
        else:
            tmp = dice[s1][2][:]
            for i in range(3):
                dice[s1][2][i] = dice[s2][i][0]
            for i in range(3):
                dice[s2][i][0] = dice[s3][0][2-i]
            for i in range(3):
                dice[s3][0][i] = dice[s4][i][2]
            for i in range(3):
                dice[s4][i][2] = tmp[2-i]

    elif side == 3:  # 뒤 (위,왼,아래,오)
        if direc == '+':  # 정면에서 봤을때 반시계임
            tmp = dice[s1][0][:]
            for i in range(3):
                dice[s1][0][i] = dice[s4][i][2]
            for i in range(3):
                dice[s4][i][2] = dice[s3][2][2-i]
            for i in range(3):
                dice[s3][2][i] = dice[s2][i][0]
            for i in range(3):
                dice[s2][i][0] = tmp[2-i]
        else:
            tmp = dice[s1][0][:]
            for i in range(3):
                dice[s1][0][i] = dice[s2][2-i][0]
            for i in range(3):
                dice[s2][i][0] = dice[s3][2][i]
            for i in range(3):
                dice[s3][2][i] = dice[s4][2-i][2]
            for i in range(3):
                dice[s4][i][2] = tmp[i]
    elif side == 4:  # 왼 (위,앞,아래,뒤)
        for i in range(3):
            tmp[i] = dice[s1][i][0]
        if direc == '+':
            for i in range(3):
                dice[s1][i][0] = dice[s4][2-i][2]
            for i in range(3):
                dice[s4][i][2] = dice[s3][2-i][0]
            for i in range(3):
                dice[s3][i][0] = dice[s2][i][0]
            for i in range(3):
                dice[s2][i][0] = tmp[i]
        else:
            for i in range(3):
                dice[s1][i][0] = dice[s2][i][0]
            for i in range(3):
                dice[s2][i][0] = dice[s3][i][0]
            for i in range(3):
                dice[s3][i][0] = dice[s4][2-i][2]
            for i in range(3):
                dice[s4][i][2] = tmp[2-i]

    elif side == 5:  # 오른(위,뒤,아래,앞)
        for i in range(3):
            tmp[i] = dice[s1][i][2]
        if direc == '+':
            for i in range(3):
                dice[s1][i][2] = dice[s4][i][2]
            for i in range(3):
                dice[s4][i][2] = dice[s3][i][2]
            for i in range(3):
                dice[s3][i][2] = dice[s2][2-i][0]
            for i in range(3):
                dice[s2][i][0] = tmp[2-i]

        else:
            for i in range(3):
                dice[s1][i][2] = dice[s2][2-i][0]
            for i in range(3):
                dice[s2][i][0] = dice[s3][2-i][2]
            for i in range(3):
                dice[s3][i][2] = dice[s4][i][2]
            for i in range(3):
                dice[s4][i][2] = tmp[i]


for tc in range(int(input())):
    set_dice()
    n = int(input())
    roll = list(input().split())

    for r_d in roll:
        # print(r_d)
        a, b = r_d[0], r_d[1]  # 돌린방향, 시계방향

        if a == 'U':
            roll_circle(0, b)
            roll_d(0, 2, 4, 3, 5, b)  # 앞,왼,뒤,오
        elif a == 'D':
            roll_circle(1, b)
            roll_d(1, 2, 5, 3, 4, b)  # 앞,오,뒤,왼
        elif a == 'F':
            roll_circle(2, b)
            roll_d(2, 0, 5, 1, 4, b)  # 위,오,아래,왼
        elif a == 'B':
            roll_circle(3, b)
            roll_d(3, 0, 4, 1, 5, b)  # 위,왼,아래,오
        elif a == 'L':
            roll_circle(4, b)
            roll_d(4, 0, 2, 1, 3, b)  # 위,앞,아래,뒤
        else:
            roll_circle(5, b)
            roll_d(5, 0, 3, 1, 2, b)  # 위,뒤,아래,앞
    for i in range(3):
        print(''.join(dice[0][i][:]))
