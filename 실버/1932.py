import sys

input = sys.stdin.readline
n = int(input())
ls = [list(map(int,input().split())) for _ in range(n)]

for i in range(1,n) :
    for j in range(len(ls[i])) :
        if j == 0 :
            ls[i][j] += ls[i-1][j]
        elif j == len(ls[i]) -1 :
            ls[i][j] += ls[i-1][j-1]
        else :
            ls[i][j] = max(ls[i][j]+ls[i-1][j], ls[i][j]+ls[i-1][j-1])

print(max(ls[-1]))