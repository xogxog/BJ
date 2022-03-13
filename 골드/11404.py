import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
city = [[987654321]*n for _ in range(n)]
for i in range(n):
    city[i][i]=0
for _ in range(m):
    a,b,c = map(int,input().split())
    if city[a-1][b-1] > c :
        city[a-1][b-1]=c
        # city[b-1][a-1]=c

for k in range(n):
    for i in range(n):
        for j in range(n):
            city[i][j]=min(city[i][j], city[i][k]+city[k][j])

for y in range(n) :
    for z in range(n):
        if city[y][z] == 987654321 :
            print(0,end=' ')
        else :
            print(city[y][z], end=' ')
    print(end='\n')
