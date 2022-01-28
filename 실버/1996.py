N = int(input())
ls = [input() for _ in range(N)]

answer = ['' for _ in range(N)]
dr = [1,1,1,0,0,-1,-1,-1]
dc = [1,0,-1,-1,1,-1,0,1]
for i in range(N) :
    for j in range(N) :
        if ls[i][j] != '.' :
            answer[i] += '*'
        else :
            tmp_tot = 0
            for k in range(8) :
                if 0<=i+dr[k]<N and 0<=j+dc[k]<N and ls[i+dr[k]][j+dc[k]] != '.' :
                    tmp_tot += int(ls[i+dr[k]][j+dc[k]])
            if tmp_tot >= 10 :
                answer[i] += 'M'
            else :
                answer[i] += str(tmp_tot)

for z in range(N):
    print(answer[z])
