import sys
input = sys.stdin.readline

N,M = map(int,input().split())

people = [[0]*(M+1)] + [[0]+list(map(int,input().split())) for _ in range(N)]
for i in range(1,N+1) :
    for j in range(1,M+1):
        people[i][j] += people[i-1][j]
for _ in range(int(input())) :
    x1,y1,x2,y2 = map(int,input().split())
    print(sum(people[x2][y1:y2+1])-sum(people[x1-1][y1:y2+1]))
