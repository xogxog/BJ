# 제자리,오,왼,위,아래
dr = [0,0,0,-1,1]
dc = [0,1,-1,0,0]

N,K = map(int,input().split()) # 0:흰. 1:빨. 2:파
chess_board = [list(map(int,input().split())) for _ in range(N)]
visited = [[]*N for _ in range(N)] # 어떤말들이 있는지 체크할,,거야,,

print(visited)
mal = [list(map(int,input().split())) for _ in range(K)] #행,열,이동방향

# 말 놓기
for i in range(len(mal)) :
    r,c = mal[i][0]-1,mal[i][1]-1
    print(r,c)
    visited[r][c].append(i)
print(visited)
turn = 1

# while True :
