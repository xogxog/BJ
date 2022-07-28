# 네트워크 복구
import sys
input = sys.stdin.readline

N,M = map(int,input().split())
ls =[[]*(N+1) for _ in range(N+1)]

for _ in range(M):
    a,b,c = map(int,input().split())
    ls[a].append((b,c))
    ls[b].append((a,c))
print(ls)