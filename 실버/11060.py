import sys
input = sys.stdin.readline
N = int(input())
jump=list(map(int,input().split()))
visit=[0] * N
if N==1:
    print(0)
else :
    for i in range(1,N) :
        print(visit)
        for j in range(i,min(N,i+jump[i-1])) :
            visit[j] = min(visit[j], visit[i-1]+1)
        if i+1<N and visit[i] == 0:
            break
        print(visit)


    if visit[-1] == 0:
        print(-1)
    else :
        print(visit[-1])