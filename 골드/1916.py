import sys
from collections import deque
input = sys.stdin.readline
N = int(input())
M = int(input())
road =[[] for _ in range(N+1)]
cost = [987654321]*(N+1)
for _ in range(M):
    s,e,w = map(int,input().split())
    road[s].append((s,e,w))
_start, _end = map(int,input().split())
q=deque()
for connect in road[_start]:
    q.append(connect)
cost[_start]=0

while q :
    _s,_e,_w = q.popleft()
    if cost[_s]+_w<cost[_e]:
        cost[_e] = cost[_s]+_w

        for connect in road[_e] : # 시작,끝,cost
            if cost[_e]+connect[2]<cost[connect[1]] :
                q.append(connect)
print(cost[_end])