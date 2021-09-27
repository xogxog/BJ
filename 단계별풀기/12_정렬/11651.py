import sys

N = int(sys.stdin.readline())
ls=[]
for _ in range(N):
    x, y = map(int, sys.stdin.readline().split())
    ls.append([y,x])
ls.sort()
for i in ls:
    print(i[1],i[0])