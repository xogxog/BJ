# 치킨배달
import sys
input = sys.stdin.readline

def chicken_shop(start) :
    global  min_ans
    if len(tmp_shop) == M :
        tmp_sum = 0
        for m in range(len(home)) :
            min_distance = 987654321
            for n in range(len(tmp_shop)) :
                min_distance = min(min_distance, abs(home[m][0]-tmp_shop[n][0])+abs(home[m][1]-tmp_shop[n][1]))
            tmp_sum += min_distance
        if tmp_sum < min_ans :
            min_ans = tmp_sum
    else :
        for l in range(start,len(chicken)) :
            tmp_shop.append(chicken[l])
            chicken_shop(l+1)
            tmp_shop.pop()


N, M = map(int,input().split())
city = [list(map(int,input().split())) for _ in range(N)]
home = []
chicken = []
tmp_shop = []
min_ans = 987654321

for i in range(N) :
    for j in range(N) :
        if city[i][j] == 1 :
            home.append((i,j))
        elif city[i][j] == 2 :
            chicken.append((i,j))

chicken_shop(0)
print(min_ans)