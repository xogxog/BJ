import sys
input = sys.stdin.readline

N,M = map(int,input().split())

people = [list(map(int,input().split())) for _ in range(N)]

for _ in range(int(input())) :
    x1,y1,x2,y2 = map(int,input().split())
    ans = 0
    tmp = people[x1-1:x2]
    for _ in range(x1-1,x2-x1+1) :
        ans += sum(tmp[_][y1-1:y2])
    print(ans)