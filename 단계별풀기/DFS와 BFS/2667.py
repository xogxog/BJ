# 2667. 단지번호 붙이기
from collections import deque
import sys
dr = [0,0,1,-1]
dc = [1,-1,0,0]

def find_start(my_map) :
    global  tot_sum
    for i in range(len(my_map)):
        for j in range(len(my_map[i])):
            if my_map[i][j] == 1:
                q.append((i, j))
                my_map[i][j] = 0
                tot_sum -= 1
                return


def find_home() :
    global tot_sum, danji_tot
    cnt = 1 # 단지 갯수

    while q :

        r,c = q.popleft()

        for m in range(4) :
            mr = r + dr[m]
            mc = c + dc[m]

            if 0<=mr<N and 0<=mc<N and my_map[mr][mc] == 1 :
                q.append((mr,mc))
                my_map[mr][mc] = 0
                tot_sum -= 1
                cnt += 1

    total.append(cnt)





N = int(input())
my_map = list(list(map(int,sys.stdin.readline().rstrip())) for _ in range(N))


tot_sum = 0 # 지도에 남은 집 갯수
for k in range(len(my_map)) :
    tot_sum += sum(my_map[k])


total = []
q= deque()


while tot_sum :
    find_start(my_map)
    find_home()

# 출력
print(len(total))
total.sort()
for t in total :
    print(t)


