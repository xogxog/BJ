import sys
from collections import deque
input = sys.stdin.readline
N,K = map(int,input().split())

coins = list(int(input()) for _ in range(N))

q = deque()
for i in range(N-1,-1,-1):
    if coins[i] <= K :
        q.append((coins[i],1))
        break
while 1:
    won, cnt = q.popleft()
    if won == K :
        print(cnt)
        break
    else :
        for i in range(N-1,-1,-1) :
            if won+coins[i] <= K :
                q.append((won+coins[i], cnt+1))
                break
