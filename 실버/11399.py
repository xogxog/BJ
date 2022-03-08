import sys
input = sys.stdin.readline
N = int(input())
ls = list(map(int,input().split()))
ls.sort()

ans = ls[0]
for i in range(1,N) :
    ls[i] += ls[i-1]
    ans += ls[i]

print(ans)