# 힙큐, 우선순위 큐!!
import sys
from collections import deque
input = sys.stdin.readline


N = int(input())
tmp_ls = []
for _ in range(N) :
    tmp_ls.append(int(input().rstrip()))
tmp_ls.sort()
tmp_ls[1] = tmp_ls[0]+tmp_ls[1]
ans = tmp_ls[1]

card = deque(tmp_ls[1:])
print(card)

while card :
