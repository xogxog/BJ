import sys
n= int(input())
ls = list(map(int,sys.stdin.readline().split()))

for _ in range(int(input())) :
    s,e = map(int, sys.stdin.readline().split())
    print(sum(ls[s-1:e]))