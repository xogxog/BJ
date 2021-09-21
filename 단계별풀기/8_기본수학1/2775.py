# 부녀회장이 될테야

T = int(input())

for tc in range(T):
    k = int(input()) # floor
    n = int(input()) # room number

    ls = [[0]*n for _ in range(k+1)]
    # print(ls)

    for i in range(len(ls)):
        for j in range(len(ls[i])):
            if i == 0:
                ls[i][j] = j+1
            elif j == 0 :
                ls[i][j] = 1
            else :
                ls[i][j] = ls[i][j-1] + ls[i-1][j]

    print(ls[k][n-1])
