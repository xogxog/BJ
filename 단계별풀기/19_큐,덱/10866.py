# find가 시간을 많이 잡아먹는다.
import sys
from collections import deque

N = int(input())
dq = deque()
for _ in range(N):
    tmp = sys.stdin.readline().rstrip().split()

    if tmp[0] == 'push_front' :
        dq.appendleft(tmp[1])

    elif tmp[0] == 'push_back' :
        dq.append(tmp[1])

    elif tmp[0] == 'pop_front' :
        if not dq :
            print(-1)
        else :
            print(dq.popleft())
    elif tmp[0] == 'pop_back' :
        if not dq :
            print(-1)
        else :
            print(dq.pop())

    elif tmp[0] == 'size':
        print(len(dq))

    elif tmp[0] == 'empty':
        if dq :
            print(0)
        else :
            print(1)

    elif tmp[0] == 'front' :
        if dq :
            print(dq[0])
        else :
            print(-1)

    else :
        if dq :
            print(dq[-1])
        else :
            print(-1)
