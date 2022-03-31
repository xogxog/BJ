import sys
from collections import deque
input = sys.stdin.readline

for _ in range(int(input())) :
    num = int(input())
    cnt = 0
    q = deque()
    q.append(1)
    q.append(2)
    q.append(3)

    while q :

        tmp = q.popleft()
        if tmp == num :
            cnt += 1
        if tmp+1 <= num :
            q.append(tmp+1)
        if tmp+2 <= num :
            q.append(tmp+2)
        if tmp+3 <= num :
            q.append(tmp+3)

    print(cnt)