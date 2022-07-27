# 텀프로젝트
import sys
input= sys.stdin.readline
sys.setrecursionlimit(100000)

def dfs(i, want_team, ls):  # 현재 학생 번호, 지목, 팀원
    global tmp_ls
    if not visited[want_team] :
        visited[want_team] = 1
        ls.append(want_team)
        dfs(want_team, student[want_team], ls)

    else : # 방문한 곳이면
        if want_team in ls : # 현재 팀원 리스트에 지목한 사람이 있는지 체크
            tmp_ls = ls[ls.index(want_team):] # 무조건 시작한 사람으로 와야하는게 아님 !
        return



for _ in range(int(input())) :
    N = int(input()) # 학생의 수
    student = [0] + list(map(int,input().split())) # 학생번호 1부터시작
    visited = [0] * (N+1)
    ans = N
    tmp_ls = []

    # 자기자신과 팀인 사람
    for j in range(1,N+1):
        if j == student[j] :
            visited[j] = 1
            ans -= 1

    for i in range(1, N+1):
        if not visited[i] :
            visited[i] = 1
            dfs(i,student[i],[i])
            # print(f'tmp_ls : {tmp_ls}')
            ans -= len(tmp_ls)
            tmp_ls = []


    print(ans)