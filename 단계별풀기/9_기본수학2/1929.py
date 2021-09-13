M, N = map(int,input().split())

for i in range(M,N+1):
    flag = 0
    for j in range(2,i//2+1):
        if i % j == 0 :
            flag=1
            break
    if flag == 0 :
        print(i)
