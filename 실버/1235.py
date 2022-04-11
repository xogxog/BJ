import sys
input = sys.stdin.readline

N = int(input())

student = list(input().rstrip() for _ in range(N))
flag=0
ans = -1
while 1 :
    stu = dict()
    for i in range(N) :
        if student[i][ans:] not in student :
            stu[student[i][ans:]] = 1
        else :
            flag = 1
    if flag or len(stu) == N :
        break
    ans -= 1
print(-ans)
