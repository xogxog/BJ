import sys
from collections import deque
N = int(sys.stdin.readline())
dq = deque([])
for _ in range(N):
    tmp = sys.stdin.readline().rstrip()
    if tmp.find('push') != -1: # find함수 특성
        order, num = tmp.split()
        dq.append(num)
    elif tmp == 'pop':
        if len(dq) > 0 :
            print(dq.popleft())
        else :
            print(-1)
    elif tmp == 'front' :
        if len(dq) > 0 :
            print(dq[0])
        else :
            print(-1)
    elif tmp == 'back' :
        if len(dq) > 0 :
            print(dq[-1])
        else :
            print(-1)
    elif tmp == 'size' :
        print(len(dq))
    elif tmp == 'empty' :
        if len(dq) > 0 :
            print(0)
        else :
            print(1)
