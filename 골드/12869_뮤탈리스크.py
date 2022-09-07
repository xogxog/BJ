import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
scv = list(map(int,input().split()))
INF = float('inf')

if n == 1 :
    if scv[0] % 9 == 0 :
        print(scv[0] // 9)
    else :
        print(scv[0] // 9 + 1)
elif n == 2 :
    x,y = scv
    dp = [[INF for _ in range(y+1)] for i in range(x+1)]
    dp[0][0] = 0
    ls = [(9,3),(3,9)]

    for j in range(x+1):
        for k in range(y+1) :
            if dp[j][k] < INF :
                for a,b in ls :
                    tmp_x = min(x,j+a)
                    tmp_y = min(y,k+b)
                    dp[tmp_x][tmp_y] = min(dp[tmp_x][tmp_y],dp[j][k]+1)

    print(dp[-1][-1])

else :
    x,y,z = scv
    dp =  [[[INF for _ in range(z+1)] for i in range(y+1)] for j in range(x+1)]
    dp[0][0][0] = 0
    ls = [(1,3,9),(1,9,3),(3,1,9),(3,9,1),(9,1,3),(9,3,1)]

    for k in range(x+1) :
        for l in range(y+1):
            for m in range(z+1) :
                if dp[k][l][m] < INF :
                    for a,b,c in ls :
                        tmp_x = min(x, k+a)
                        tmp_y = min(y, l+b)
                        tmp_z = min(z, m+c)
                        dp[tmp_x][tmp_y][tmp_z] = min(dp[tmp_x][tmp_y][tmp_z], dp[k][l][m]+1)

    print(dp[-1][-1][-1])
