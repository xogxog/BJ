import sys
input = sys.stdin.readline

N,C = map(int,input().split())
ls = []
for _ in range(N):
    ls.append(int(input()))
ls.sort()

start, mid, end = 0, N//2, N-1