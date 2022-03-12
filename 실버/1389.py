import sys
input = sys.stdin.readline
N,M = map(int,input().split())
ls=[[987654321]*N for _ in range(N)]

for i in range(N):
    ls[i][i] = 0
for _ in range(M):
    a,b = map(int,input().split())
    ls[a-1][b-1] = 1
    ls[b-1][a-1] = 1

for k in range(N) :
    for i in range(N) :
        for j in range(N) :
            ls[i][j] = min(ls[i][j], ls[i][k]+ls[k][j])

min_value = 987654321
ans = 0
for z in range(N-1,-1,-1):
    if min_value >= sum(ls[z]) :
        min_value = sum(ls[z])
        ans = z
print(ans+1) #...0부터 시작했으니까 ... +1 해줘야한다.