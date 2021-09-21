M, N = map(int,input().split())

for i in range(M,N+1):
    flag = 0
    if i == 0 or i == 1:
        continue
    m = round(i**(1/2))
    # print(f'm : {m}')
    for j in range(2,m+1):
        if i % j == 0 :
            flag=1
            break
    if flag == 0 :
        print(i)
