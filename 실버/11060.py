import sys
input = sys.stdin.readline
N = int(input())
jump=list(map(int,input().split()))
visit=[0] * N

for i in range(1,N):
    for j in range(i,min(N,i+jump[i-1])) :
        if visit[j] == 0 :
            visit[j]=visit[i-1]+1
        elif visit[i-1]+1 < visit[j] :
            visit[j]=visit[i-1]+1

if visit[-1] == 0 :
    print(-1)
else :
    print(visit[-1])