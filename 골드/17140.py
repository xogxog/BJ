def my_sort(my_list):
    max_r_len = 0  # 가장 긴 리스트 기준으로 정렬해주어야 하므로
    for i in range(len(my_list)):
        tmp_dict = dict()
        for j in range(len(my_list[i])):

            if my_list[i][j] == 0:  # 0은 정렬에 끼면 안 됨!
                continue
            if my_list[i][j] in tmp_dict:
                tmp_dict[my_list[i][j]] += 1
            else:
                tmp_dict[my_list[i][j]] = 1
        tmp_list = list(zip(tmp_dict.keys(), tmp_dict.values()))  # 수 ,등장횟수 [(),(),()] 형태로 변환
        tmp_list.sort(key=lambda x: x[0])  # 수가 커지는 순 정렬
        tmp_list.sort(key=lambda x: x[1])  # 등장횟수 커지는 순 정렬

        # 가장 긴 행 뽑기 ( 100제한 )
        if len(tmp_list) * 2 <= 100 and max_r_len < len(tmp_list) * 2:
            max_r_len = len(tmp_list) * 2

        # 정렬한 행 채워넣기 (100개까지만)
        tmp_list2 = []
        for k in range(len(tmp_list)):
            if k == 50 :
                break
            tmp_list2.append(tmp_list[k][0])
            tmp_list2.append(tmp_list[k][1])
        my_list[i] = tmp_list2

    # 0 채워주기
    for l in range(len(my_list)):
        if len(my_list[l]) < max_r_len:
            my_list[l] += [0] * (max_r_len - len(my_list[l]))
    return (len(my_list), max_r_len, my_list) # 행, 열, 리스트 반환

r, c, k = map(int, input().split())  # 행, 열, 값
my_list = [list(map(int, input().split())) for _ in range(3)]
cnt_r = 3
cnt_c = 3
t = 0  # time

while True:
    # r,c 범위 지정해 줘야한다

    if r-1 < cnt_r and c-1 < cnt_c and my_list[r - 1][c - 1] == k :
        print(t)
        break


    # 행 정렬 수행
    if cnt_r >= cnt_c :
        cnt_r, cnt_c, my_list = my_sort(my_list)

    # 열 정렬 수행
    else :
        #  오른쪽으로 90도 돌리기
        swap_list = [[0]*cnt_r for _ in range(cnt_c)] # 뒤집어 줄 리스트

        for m in range(len(my_list)) :
            for n in range(len(my_list[m])):
                swap_list[n][m] = my_list[m][n]

        # my_list = list(map(list,zip(*my_list)))

        cnt_r, cnt_c, returned_swap_list = my_sort(swap_list)

        # 다시 -90도 돌리기
        my_list = [[0]*cnt_r for _ in range(cnt_c)]

        for o in range(len(returned_swap_list)) :
            for p in range(len(returned_swap_list[o])):
                my_list[p][o] = returned_swap_list[o][p]

        # 이걸 안해서 자꾸 막힘 .....
        cnt_r, cnt_c = cnt_c, cnt_r # 돌렸으므로 , r과 c를 바꿔야 한다.


    t += 1

    if t > 100 :
        print(-1)
        break
