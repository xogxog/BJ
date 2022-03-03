import sys

def dig(n,B) :
    global min_time, min_ground
    tmp_time = 0
    for i in range(N):
        for j in range(M):
            if ground[i][j]==n :
                continue
            elif ground[i][j] < n :
                up = n-ground[i][j]
                tmp_time += up
                B -= up
            elif ground[i][j] > n :
                down = ground[i][j] - n
                tmp_time += (down*2)
                B += down
        if tmp_time > min_time :
            return
    if B >= 0 and tmp_time<=min_time : # 남은 블록이 있고, 시간 짧은경우
        min_time = tmp_time
        if min_ground < n :
            min_ground = n


N,M,B = map(int,sys.stdin.readline().split())

min_ground = 987654321
max_ground = -1

ground =[]
for i in range(N):
    ground.append(list(map(int,sys.stdin.readline().split())))
    if max(ground[i]) > max_ground :
        max_ground = max(ground[i])
    if min(ground[i]) < min_ground :
        min_ground = min(ground[i])
# print(min_ground, max_ground, ground)
min_time = 987654321
max_hei = -1

for k in range(min_ground,max_ground+1) :
    dig(k,B)
print(min_time,min_ground)


