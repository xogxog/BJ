import sys
input = sys.stdin.readline
# 제자리,오,왼,위,아래(1,2,3,4)
dr = [0,0,0,-1,1]
dc = [0,1,-1,0,0]

N,K = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(N)] # 0:흰. 1:빨. 2:파
location = {} # 체스판위에 말들 쌓기위해 (key : 좌표, value : [말번호]) -> 방향은 필요없을까?
curr_mal =[] # 말 별 현재위치
for i in range(N):
    for j in range(N):
        location[i,j]=[]

for i in range(K) :
    mal = list(map(int,input().split())) #행,열,이동방향
    location[(mal[0]-1,mal[1]-1)].append(i) # 말 번호
    curr_mal.append([i,mal[0]-1,mal[1]-1,mal[2],len(location[(mal[0]-1,mal[1]-1)])]) #말번호(0부터),행,열,이동방향, 몇번째쌓여있는지(1부터)
print(location)
print(location[(1,0)])
time = 1

while time <= 1000 :
    # 말 옮기기
    for i in range(K) :

        num,r,c,direc,ord = curr_mal[i] #몇번째 말,행,열,방향,몇번째(1부터~)

        nr = r+dr[direc]
        nc = c+dc[direc]

        if 0<=nr<N and 0<=nc<N :
            if board[nr][nc] == 0 : # 흰색인 경우

                location[(r,c)] = location[(r,c)][0:ord] # 0~현재말전까지 가만 냅두기
                location[(nr,nc)].append(location[(r,c)][ord-1:]) # 말 옮기기

                for mal_number in location[(r,c)][ord-1:] :
                    curr_mal[mal_number][1] = nr
                    curr_mal[mal_number][2] = nc
                    curr_mal[mal_number][4] = location[(nr,nc)].index(mal_number)+1

            elif board[nr][nc] == 1 : #빨간색인 경우

                location[(r, c)] = location[(r, c)][0:ord]  # 0~현재말전까지 자르기
                reord_location = location[(r,c)][ord-1:][::-1] # 순서 반대로

                location[(nr,nc)].append(reord_location)

                for mal_number in reord_location :
                    curr_mal[mal_number][1] = nr
                    curr_mal[mal_number][2] = nc
                    curr_mal[mal_number][4] = location[(nr, nc)].index(mal_number) + 1

            else : # 파란색의 경우(하ㅏ ,,,,,,)




    time +=1

a=[1,2,3,4,5,6,7,8,9]
print(a[:2:-1]) # [9, 8, 7, 6, 5, 4]
print(a[4:1:-1]) # [5, 4,3]
print(a[::-1])
