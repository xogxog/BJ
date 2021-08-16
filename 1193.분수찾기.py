def MySearch(x) :
    # 오, 왼아래, 아래, 오른위
    dr = [0, 1, 1, -1]  # row
    dc = [1, -1, 0, 1]  # column

    # 방향조작
    k = 0
    k_2 = 1 #대각선 증가 갯수
    cnt = 1

    row = 0  # 현재위치 row
    col = 0  # 현재위치 col
    while cnt < x:

        # 오른쪽 한번 / 아래 한번
        row += dr[k]
        col += dc[k]
        cnt += 1
        k = (k+1)%4
        if cnt == x: return row,col

        # 왼 아래 / 오른 위
        for _ in range(0,k_2):
            row += dr[k]
            col += dc[k]
            cnt += 1
            if cnt == x: return row,col
        k_2 += 1
        k = (k+1)%4

    return row,col







x = int(input())
curr_loca = MySearch(x)

#print(curr_loca)

print(str(curr_loca[0]+1)+'/'+str(curr_loca[1]+1))