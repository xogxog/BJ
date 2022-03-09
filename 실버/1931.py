import sys
input = sys.stdin.readline

N = int(input())

meeting = [tuple(map(int,input().split())) for _ in range(N)]

meeting.sort(key=lambda x : (x[1],x[0])) # x[1]졍렬하고 그 안에서 x[0] 정렬하는 방식
print(meeting)
answer=[meeting[0]]

for i in range(1,N) :
    if answer[-1][1]<=meeting[i][0] :
        answer.append(meeting[i])

print(len(answer))
