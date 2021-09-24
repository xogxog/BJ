

def draw(chess) :
    cnt = 0
    cnt2 = 0
    # if chess[0][0] == 'W' :
    for k in range(len(chess)) :
        for l in range(len(chess[k])) :
            if (k % 2 == 0 and l % 2 == 0) or (k % 2 and l % 2) : # (짝,짝), (홀,홀)
                if chess[k][l] != 'W':
                    cnt += 1
            else :
                if chess[k][l] != 'B':
                    cnt += 1

    # if chess[0][0] == 'B' : # 시작이 B 인경우
    for k in range(len(chess)):
        for l in range(len(chess[k])) :
            if (k % 2 == 0 and l % 2 == 0) or (k % 2 and l % 2) : # (짝,짝), (홀,홀)
                if chess[k][l] != 'B':
                    cnt2 += 1
            else :
                if chess[k][l] != 'W':
                    cnt2 += 1

    return min(cnt, cnt2)


n, m = map(int, input().split())  # 행, 열

not_chess = list(list(input()) for _ in range(n))
# print(not_chess)
min_tot = 100000
for i in range(n - 7):
    for j in range(m - 7):
        sub_tot = draw([chess2[j:j + 8] for chess2 in not_chess[i:i + 8]])
        if sub_tot < min_tot :
            min_tot = sub_tot


print(min_tot)
