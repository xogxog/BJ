

def diff(A,B) :
    # print(A,B)
    global flag
    sub_A = 0
    sub_B = 0
    for i in range(0, (N//2) - 1) :
        for j in range(i+1, N//2) :
            sub_A += synergy[A[i]][A[j]]

    for i in range(0, (N//2) - 1) :
        for j in range(i+1, N//2) :
            sub_B += synergy[B[i]][B[j]]

    tot = abs(sub_A - sub_B)
    if tot == 0 :
        flag = 1

    return tot


def taste(idx, s_idx) :
    global min_tot
    if s_idx == N // 2 :

        B = []
        for j in range(N) :
            if j not in A :
                B.append(j)
        sub_tot = diff(A,B)
        if min_tot > sub_tot :
            min_tot = sub_tot
        return

    if flag :
        return


    for i in range(idx,N) :
        A[s_idx] = i
        visited[i] = 1
        taste(i+1, s_idx+1)
        visited[i] = 0





N = int(input())
soccer = [list(map(int,input().split())) for _ in range(N)]

synergy = [[0]*N for _ in range(N)]
for i in range(0,N):
    for j in range(i+1,N) :
        synergy[i][j] = soccer[i][j] + soccer[j][i]


flag = 0
min_tot = 987654321
visited = [0] * N
A= [0] * (N // 2)

taste(0,0)
print(f'{min_tot}')