n,k = map(int,input().split())
ls = [list(map(int,input().split())) for _ in range(n)]
ans_ls = [[0]*(n*k) for _ in range(n*k)]


for i in range(n) :
    tmp = []
    t = 0
    for j in range(n):
        tmp += [ls[i][j]]*k # append 와 +=는 다르다 !!!!!!!!!!!!
    while t <k :
        print(*tmp)
        t += 1
