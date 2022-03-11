# import sys 해야 시간 초과 안남
import sys
input = sys.stdin.readline
N,M = map(int,input().split())

ls = list(map(int,input().split()))

for i in range(1,N) :
    ls[i] += ls[i-1]

for _ in range(M):
    a,b = map(int,input().split())
    if a == 1 :
        print(ls[b-1])
    else :
        print(ls[b - 1]-ls[a-2])
