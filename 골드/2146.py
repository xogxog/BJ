import sys
from collections import deque
input = sys.stdin.readline
# 상 우 하 좌
dr = [1,0,-1,0]
dc = [0,1,0,-1]

def land_chk(q) :
    while q :
        






N = int(input())
island = [list(map(int,input().split())) for _ in range(N)]
my_island = [[0]*N for _ in range(N)]
land_num = 1
q = deque()
for i in range(N):
    for j in range(N):
        if island == 1 :
            q.append((i,j))
            land_chk(q)