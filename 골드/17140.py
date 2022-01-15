r, c, k = map(int, input().split())  # 행, 열, 값
my_list = [list(map(int, input().split())) for _ in range(3)]
t = 0  # time
cnt_r = 3 # 행의 갯수
cnt_c = 3 # 열의 갯수
while t < 100:
    if my_list[r - 1][c - 1] == k:
        print(t)
        break

    # 행 정렬 수행
    if cnt_r >= cnt_c :
        max_r_len = 0
        for r_list in my_list :
            tmp_list = []
            if t == 0 :
                for num in r_list :
                    if num in  :
                        tmp_dic[num] += 1
                    else :
                        tmp_dic[num] = 1
                for key, value in tmp_dic.items() :

            else :
    else :

    time += 1
