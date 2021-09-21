N = int(input())
ls = list(map(int,input().split()))
cnt = 0
# print(ls)

for i in range(len(ls)):
    flag = 0
    if ls[i] == 0 or ls[i] == 1:
        continue
    for j in range(2, ls[i]) :
        if ls[i] % j == 0 :
            flag = 1
            break
    if flag == 1 :
        continue
    elif flag == 0 :
        cnt += 1

print(cnt)
