from collections import deque
N,K = map(int,input().split())
belt = deque(list(map(int,input().split())))
robot = deque([0] * N) # 로봇
time = 0
num = 0
while True :
    if num >= K :
        break
    time += 1 # 시간 +1
    belt.rotate(1) # 벨트돌리기
    robot.rotate(1)
    if robot[N-1] == 1 : # 내리는위치에 오면 그 즉시 내린다.
        robot[N-1] = 0
    for i in range(N-2,-1,-1) : # 로봇 한 칸씩 전진!
        if robot[i] == 1 and robot[i+1]==0 and belt[i+1] >0 : #다음칸에 로봇없고, 벨트내구도 0보다 커야함
            robot[i] = 0
            belt[i + 1] -= 1
            if i+1 != N-1 : # 내리는 자리가 아니면 로봇 옮기기 / 내리는 자리면 그 즉시 내리므로 올리는 의미 X
                robot[i+1] = 1
            if belt[i + 1] == 0 :
                num += 1
    if belt[0] > 0 and robot[0] == 0 : # 내구도 0보다 크고, 로봇이 없다면 ( 로봇 올리기 )
        robot[0] = 1
        belt[0] -= 1
        if belt[0] == 0 :
            num += 1


print(time)
